@echo off
chcp 65001 >nul
title Очистка списка скачанных модов
color 0C

echo ============================================
echo   Очистка списка скачанных модов
echo ============================================
echo.
echo ВНИМАНИЕ! Это удалит список всех скачанных модов.
echo Скрипт снова начнет скачивать все моды заново.
echo.
pause

if exist downloaded_mods.txt (
    del downloaded_mods.txt
    echo.
    echo ✓ Список скачанных модов удален!
) else (
    echo.
    echo Файл downloaded_mods.txt не найден.
)

echo.
pause
