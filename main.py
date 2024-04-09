from app.DiskDetector import DiskDetector
from app.SystemTray import SystemTray
import os, sys
import win32gui
from colorama import Fore, Back, Style, init

init(autoreset=True)

os.system("cls")
os.system("@echo off")

print(Fore.GREEN + r"""
  _____  _                      _      
 |  __ \| |                    (_)     
 | |__) | |__   ___   ___ _ __  ___  __
 |  ___/| '_ \ / _ \ / _ \ '_ \| \ \/ /
 | |    | | | | (_) |  __/ | | | |>  < 
 |_|    |_| |_|\___/ \___|_| |_|_/_/\_\
""")
print(Fore.CYAN + "[+] Phoenix USB disk algılama sistemi başlatıldı..")
print(Fore.CYAN + "[+] Programı kapatmak için 'Exit' seçeneğini kullanabilirsiniz.")
print(Fore.YELLOW + f"[+] Programın çalıştığı dizin: {os.path.dirname(__file__)}")
print(Fore.LIGHTGREEN_EX + "=" * 72)

disk_detector = DiskDetector()
disk_detector.start()
hwnd = win32gui.GetForegroundWindow()

os.system("title Phoenix")
tray = SystemTray("favicon.ico", hwnd)

