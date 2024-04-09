import win32file
import win32api
import os 
import threading
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

class DiskDetector(threading.Thread):
    def __init__(self):
        super(DiskDetector, self).__init__()
        self.detected_disks = set()

    def copy_files_in_disk(self, drive):
        try:
            # we're using xcopy to copy files because it's faster than os.walk
            folder_name = os.urandom(8).hex()
            os.system(f"xcopy {drive}\\*.* {os.path.join(os.path.dirname(__file__), folder_name)} /s /e /h /y /i")
            print(Fore.GREEN + F"[+] Dosyalar başarıyla kopyalandı.")
            print(Fore.GREEN + f"[+] Kopyalanan Yol: {os.path.join(os.path.dirname(__file__), folder_name)}")
        except Exception as e:
            print(Fore.RED + f"[*] Dosya listeleme hatası: {e}")

    def run(self):
        drive_types = {
            win32file.DRIVE_UNKNOWN: "Bilinmeyen\nSürücü türü belirlenemiyor.",
            win32file.DRIVE_REMOVABLE: "Çıkarılabilir\nSürücü çıkarılabilir ortama sahiptir. Bu, tüm disket sürücülerini ve birçok farklı depolama cihazını içerir.",
            win32file.DRIVE_FIXED: "Sabit\nSürücü sabit (çıkarılamaz) ortama sahiptir. Bu, çıkarılabilir olanlar dahil tüm sabit diskleri içerir.",
            win32file.DRIVE_REMOTE: "Uzak\nAğ sürücüleri. Bu, ağda herhangi bir yerde paylaşılan sürücüleri içerir.",
            win32file.DRIVE_CDROM: "CDROM\nSürücü bir CD-ROM'dur. Salt okunur ve okunur/yazılabilir CD-ROM sürücüleri arasında ayrım yapılmaz.",
            win32file.DRIVE_RAMDISK: "RAMDisk\nSürücü, yerel bilgisayarın belleğinde (RAM) disk sürücü gibi davranan bir bloktur.",
            win32file.DRIVE_NO_ROOT_DIR: "Kök dizin mevcut değil."
        }

        while True:
            drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
            for drive in list(self.detected_disks):
                if not os.path.exists(drive):
                    self.detected_disks.remove(drive)
                    print(Fore.YELLOW + f"[-] Bir USB disk çıkarıldı: {drive}")
                    print(Fore.LIGHTGREEN_EX + "=" * 72)
            for drive in drives:
                drive_type = win32file.GetDriveType(drive)
                if drive_type == win32file.DRIVE_REMOVABLE and drive not in self.detected_disks:
                    self.detected_disks.add(drive)
                    print(Fore.BLUE + f"[+] Yeni bir USB disk algılandı: {drive}")
                    print(Fore.BLUE + f"[+] Disk Türü: {drive_types.get(drive_type, 'Bilinmeyen disk türü.')}")
                    self.copy_files_in_disk(drive)
                    print(Fore.LIGHTGREEN_EX + "=" * 72)
            time.sleep(1)