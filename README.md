# Vortex Auto Downloader

Автоматический скрипт для загрузки модов через Vortex Mod Manager и Nexus Mods.

🇷🇺 [Русская версия](#russian) | 🇬🇧 [English version](#english)

---

<a name="russian"></a>
## 🇷🇺 Русская версия

### 📋 Описание

Скрипт автоматизирует процесс загрузки модов:
1. Находит кнопку "Download manually" в Vortex
2. Нажимает на неё
3. Переключается в браузер (Chrome)
4. Находит и нажимает кнопку "Slow download" на сайте Nexus Mods
5. Возвращается в Vortex и ждёт следующий мод

### ⚙️ Требования

- Windows 10/11
- Python 3.8 или новее
- Vortex Mod Manager
- Google Chrome

### 📦 Установка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/MonD24/nexusmods_autodl.git
cd nexusmods_autodl
```

2. **Установите зависимости:**
```bash
pip install -r requirements.txt
```
Или вручную:
```bash
pip install pyautogui pygetwindow psutil pywin32 pillow
```

### 🖼️ Подготовка скриншотов

**Важно!** Перед запуском нужно создать скриншоты кнопок:

#### 1. Кнопка в Vortex (`button.png`)
- Откройте Vortex с окном загрузки мода
- Нажмите `Win + Shift + S`
- Выделите **только кнопку** "Download manually"
- Сохраните как `button.png` в папку со скриптом

![Пример кнопки Vortex](https://i.imgur.com/example.png)

#### 2. Кнопка в браузере (`browser_button.png`)
- Откройте страницу скачивания на Nexus Mods
- Нажмите `Win + Shift + S`
- Выделите **только кнопку** "Slow download"
- Сохраните как `browser_button.png` в папку со скриптом

![Пример кнопки браузера](https://i.imgur.com/example2.png)

### 🚀 Использование

#### Способ 1: Через .bat файл (рекомендуется)
1. Запустите Vortex
2. Откройте Chrome с любой страницей Nexus Mods
3. Двойной клик на `run_vortex_downloader.bat`

#### Способ 2: Через командную строку
```bash
python vortex_button_click_full.py
```

### ⚙️ Настройка

Откройте `vortex_button_click_full.py` и измените параметры:

```python
CONFIDENCE_LEVEL = 0.55  # Точность поиска кнопки (0.0-1.0)
DEBUG_SCREENSHOTS = True  # Включить отладочные скриншоты
```

**Координаты области с названием мода** (если нужно настроить):
```python
mod_name_region = (140, 80, 360, 120)  # (left, top, right, bottom)
```

### 🛠️ Решение проблем

#### Кнопка не находится
1. Пересоздайте скриншот кнопки (только саму кнопку, без лишних краёв)
2. Понизьте `CONFIDENCE_LEVEL` до 0.45-0.50
3. Проверьте, что масштаб Windows установлен на 100%

#### Скрипт нажимает не на ту кнопку
1. Повысьте `CONFIDENCE_LEVEL` до 0.60-0.70
2. Убедитесь, что скриншот кнопки точный

#### Vortex не активируется
- Закройте VS Code или переименуйте файл скрипта (убрать "vortex" из названия)

### 📝 Структура проекта

```
nexusmods_autodl/
├── vortex_button_click_full.py    # Основной скрипт
├── run_vortex_downloader.bat      # Запуск одним кликом
├── button.png                      # Скриншот кнопки Vortex (создайте сами)
├── browser_button.png              # Скриншот кнопки браузера (создайте сами)
├── requirements.txt                # Зависимости Python
├── LICENSE                         # Лицензия MIT
└── README.md                       # Документация
```

### 🤝 Вклад

Приветствуются Pull Request'ы и Issues!

### 📄 Лицензия

MIT License

---

<a name="english"></a>
## 🇬🇧 English Version

### 📋 Description

Script automates mod downloading process:
1. Finds "Download manually" button in Vortex
2. Clicks it
3. Switches to browser (Chrome)
4. Finds and clicks "Slow download" button on Nexus Mods
5. Returns to Vortex and waits for next mod

### ⚙️ Requirements

- Windows 10/11
- Python 3.8 or newer
- Vortex Mod Manager
- Google Chrome

### 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/MonD24/nexusmods_autodl.git
cd nexusmods_autodl
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install pyautogui pygetwindow psutil pywin32 pillow
```

### 🖼️ Preparing Screenshots

**Important!** You need to create button screenshots before running:

#### 1. Vortex Button (`button.png`)
- Open Vortex with mod download window
- Press `Win + Shift + S`
- Select **only the button** "Download manually"
- Save as `button.png` in script folder

#### 2. Browser Button (`browser_button.png`)
- Open download page on Nexus Mods
- Press `Win + Shift + S`
- Select **only the button** "Slow download"
- Save as `browser_button.png` in script folder

### 🚀 Usage

#### Method 1: Via .bat file (recommended)
1. Start Vortex
2. Open Chrome with any Nexus Mods page
3. Double-click `run_vortex_downloader.bat`

#### Method 2: Via command line
```bash
python vortex_button_click_full.py
```

### ⚙️ Configuration

Open `vortex_button_click_full.py` and change parameters:

```python
CONFIDENCE_LEVEL = 0.55  # Button search accuracy (0.0-1.0)
DEBUG_SCREENSHOTS = True  # Enable debug screenshots
```

**Mod name region coordinates** (if you need to adjust):
```python
mod_name_region = (140, 80, 360, 120)  # (left, top, right, bottom)
```

### 🛠️ Troubleshooting

#### Button not found
1. Recreate button screenshot (only the button, no extra edges)
2. Lower `CONFIDENCE_LEVEL` to 0.45-0.50
3. Check that Windows scaling is set to 100%

#### Script clicks wrong button
1. Increase `CONFIDENCE_LEVEL` to 0.60-0.70
2. Make sure button screenshot is precise

#### Vortex doesn't activate
- Close VS Code or rename script file (remove "vortex" from name)

### 📝 Project Structure

```
nexusmods_autodl/
├── vortex_button_click_full.py    # Main script
├── run_vortex_downloader.bat      # One-click launcher
├── button.png                      # Vortex button screenshot (create yourself)
├── browser_button.png              # Browser button screenshot (create yourself)
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
└── README.md                       # Documentation
```

### 🤝 Contributing

Pull Requests and Issues are welcome!

### 📄 License

MIT License

---

## 💡 Features

- ✅ Automatic window activation and switching
- ✅ Duplicate mod detection (checks mod name changes)
- ✅ Multiple confidence levels for button detection
- ✅ Grayscale fallback for better detection
- ✅ Browser auto-detection after button click
- ✅ Error handling and retry logic
- ✅ Easy one-click launch via .bat file

## 🔧 Advanced Settings

### Custom Browser
Change browser keyword in script:
```python
BROWSER_WINDOW_KEYWORD = "Firefox"  # or "Edge", etc.
```

### Adjust Wait Times
```python
time.sleep(2)  # Change wait time in seconds
```

### Debug Mode
```python
DEBUG_SCREENSHOTS = True  # Saves screen.png for debugging
```

---

**Made with ❤️ for the modding community**
