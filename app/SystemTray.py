import os
import pystray
from pystray import MenuItem as item
from PIL import Image
import win32gui
import win32con


class SystemTray:
    def __init__(self, icon_path, hwnd):
        self.hwnd = hwnd
        self.icon = pystray.Icon("SystemTrayIcon", Image.open(icon_path), "Phoenix", menu=self.menu())
        self.icon.run()
        
    def menu(self):
        return [
            item('Göster', self.show_window),
            item('Gizle', self.hide_window),
            item('Çıkış', self.exit_app)
        ]
        
    def show_window(self, icon, item):
        self.set_window_visibility(win32con.SW_SHOWNORMAL)

    def hide_window(self, icon, item):
        self.set_window_visibility(win32con.SW_HIDE)
    
    def set_window_visibility(self, visibility):
        hwnd = self.hwnd
        win32gui.ShowWindow(hwnd, visibility)

    def exit_app(self, icon, item):
        icon.stop()
        os._exit(0)