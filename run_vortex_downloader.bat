@echo off
chcp 65001 >nul
title Vortex Auto Downloader
color 0A

echo ============================================
echo   Vortex Auto Downloader
echo ============================================
echo.
echo Запуск скрипта автоматической загрузки модов...
echo.
echo Убедитесь что:
echo  - Vortex запущен
echo  - Chrome открыт с нужной вкладкой
echo  - Файлы button.png и browser_button.png созданы
echo.
echo Для остановки нажмите Ctrl+C
echo.
pause

python vortex_button_click_full.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ============================================
    echo ОШИБКА! Скрипт завершился с ошибкой.
    echo ============================================
    pause
)
