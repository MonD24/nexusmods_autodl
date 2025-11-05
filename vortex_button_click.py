import pyautogui
import time

# Дайте время открыть нужное окно Vortex
print("Откройте окно Vortex и убедитесь, что кнопка видна. Скрипт начнёт через 5 секунд...")
time.sleep(5)

# Поиск кнопки на экране по изображению (замените 'button.png' на ваш файл)
button_location = pyautogui.locateCenterOnScreen('button.png', confidence=0.8)
if button_location:
    pyautogui.moveTo(button_location)
    pyautogui.click()
    print("Кнопка нажата!")
else:
    print("Кнопка не найдена. Проверьте скриншот и положение окна.")
