import pyautogui
import time
import psutil
import pygetwindow as gw
import sys
import win32gui
import win32con

VORTEX_PROCESS_NAME = "Vortex.exe"
VORTEX_WINDOW_KEYWORD = "Vortex"
BROWSER_WINDOW_KEYWORD = "Chrome"
BUTTON_IMAGE = "button.png"  # Кнопка в Vortex
BROWSER_BUTTON_IMAGE = "browser_button.png"  # Кнопка в браузере
CONFIDENCE_LEVEL = 0.55  # Порог совпадения (чем ниже, тем менее строгий поиск)
DEBUG_SCREENSHOTS = False  # Сохранять скриншоты для отладки (отключено для скорости)
pyautogui.PAUSE = 0.5  # Пауза между действиями pyautogui

# Поиск процесса Vortex
vortex_pid = None
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] and VORTEX_PROCESS_NAME.lower() in proc.info['name'].lower():
        vortex_pid = proc.info['pid']
        break

if not vortex_pid:
    print("Процесс Vortex не найден. Запустите Vortex и попробуйте снова.")
    sys.exit(1)

# Поиск окна браузера
browser_windows = gw.getWindowsWithTitle(BROWSER_WINDOW_KEYWORD)
if not browser_windows:
    print("Окно браузера не найдено. Откройте Chrome и нужную вкладку.")
    sys.exit(1)

browser_window = browser_windows[0]

# Поиск и активация окна Vortex
all_windows = gw.getWindowsWithTitle(VORTEX_WINDOW_KEYWORD)
if not all_windows:
    print("Окно Vortex не найдено. Убедитесь, что программа запущена.")
    sys.exit(1)

# Фильтруем окна - исключаем VS Code, ищем настоящий Vortex
vortex_window = None
for win in all_windows:
    title = win.title.lower()
    # Исключаем VS Code и другие редакторы
    if "visual studio code" not in title and "vscode" not in title and ".py" not in title:
        vortex_window = win
        print(f"Найдено окно Vortex: {win.title}")
        break

if not vortex_window:
    print("Настоящее окно Vortex не найдено (найдены только окна редактора).")
    print("Доступные окна с 'Vortex' в названии:")
    for win in all_windows:
        print(f"  - {win.title}")
    sys.exit(1)

def activate_window(window, window_name="Окно"):
    """Надежная активация окна"""
    try:
        hwnd = window._hWnd
        print(f"Активирую {window_name} (HWND: {hwnd}, Title: {window.title})...")
        # Восстановить, если свернуто
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(0.5)
        # Вывести на передний план
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.3)
        # Максимизировать
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        time.sleep(0.3)
        
        # Проверяем, что окно действительно активно
        active_hwnd = win32gui.GetForegroundWindow()
        active_title = win32gui.GetWindowText(active_hwnd)
        print(f"Активное окно: {active_title} (HWND: {active_hwnd})")
        return True
    except Exception as ex:
        print(f"Ошибка активации через win32gui: {ex}. Пробую стандартный метод...")
        # Fallback на стандартный метод
        window.restore()
        window.activate()
        window.maximize()
        return True

# Первоначальная активация Vortex
print("\n--- Первоначальная активация Vortex ---")
activate_window(vortex_window, "Vortex")
print("Ожидание 2 секунды...")
time.sleep(2)

first_iteration = True

while True:
    # 1. Ищем кнопку в Vortex (не активируем окно каждый раз - оно откроется само)
    if not first_iteration:
        print("\n--- Цикл: Проверка Vortex ---")
        print("Ожидание 2 секунды перед поиском кнопки...")
        time.sleep(2)
    else:
        print("\n--- Цикл: Первый поиск кнопки ---")
        first_iteration = False
    
    # Сохраним скриншот для отладки
    if DEBUG_SCREENSHOTS:
        screenshot = pyautogui.screenshot()
        screenshot.save("debug_vortex_screen.png")
        print(f"Скриншот экрана сохранён: debug_vortex_screen.png")
        print(f"Ищу кнопку в файле: {BUTTON_IMAGE} с порогом confidence={CONFIDENCE_LEVEL}")
    
    try:
        import os
        from PIL import Image, ImageChops
        import hashlib
        
        if not os.path.exists(BUTTON_IMAGE):
            print(f"ОШИБКА: Файл {BUTTON_IMAGE} не найден! Создайте скриншот кнопки.")
            button_location = None
        else:
            # Пробуем найти с разными порогами (более строгие значения)
            button_location = None
            for confidence in [CONFIDENCE_LEVEL, CONFIDENCE_LEVEL - 0.05, CONFIDENCE_LEVEL - 0.1]:
                try:
                    print(f"Попытка поиска с confidence={confidence:.2f}...")
                    button_location = pyautogui.locateCenterOnScreen(BUTTON_IMAGE, confidence=confidence, grayscale=False)
                    if button_location:
                        print(f"✓ Кнопка найдена на координатах: {button_location} (confidence={confidence:.2f})")
                        break
                except pyautogui.ImageNotFoundException as e:
                    # Попробуем с grayscale
                    try:
                        button_location = pyautogui.locateCenterOnScreen(BUTTON_IMAGE, confidence=confidence, grayscale=True)
                        if button_location:
                            print(f"✓ Кнопка найдена (grayscale) на координатах: {button_location} (confidence={confidence:.2f})")
                            break
                    except:
                        print(f"  Не найдено с confidence={confidence:.2f}")
                        continue
    except Exception as e:
        print(f"✗ Ошибка поиска кнопки: {e}")
        button_location = None
    
    if button_location:
        pyautogui.moveTo(button_location)
        pyautogui.click()
        print("Кнопка в Vortex нажата! Ожидаю автоматического открытия браузера...")
        
        # 2. Ждём, пока браузер откроется автоматически
        print("\n--- Ожидание открытия браузера (он откроется сам после клика) ---")
        
        # Ждем появления кнопки в браузере (до 10 попыток по 2 секунды)
        browser_button_found = False
        for attempt in range(10):
            try:
                browser_button_location = pyautogui.locateCenterOnScreen(BROWSER_BUTTON_IMAGE, confidence=CONFIDENCE_LEVEL)
            except pyautogui.ImageNotFoundException as e:
                if attempt == 0:
                    print(f"Кнопка в браузере не найдена: {e}")
                browser_button_location = None
            
            if browser_button_location:
                pyautogui.moveTo(browser_button_location)
                pyautogui.click()
                print("Кнопка в браузере нажата! Возвращаюсь в Vortex и жду новую кнопку...")
                browser_button_found = True
                time.sleep(2)
                break
            else:
                print(f"Попытка {attempt + 1}/10: Кнопка в браузере не найдена. Жду 2 секунды...")
                time.sleep(2)
        
        if not browser_button_found:
            print("Кнопка в браузере так и не появилась. Возвращаюсь в Vortex...")
            time.sleep(1)
    else:
        print("Кнопка в Vortex не найдена. Жду 2 секунды...")
        time.sleep(2)
