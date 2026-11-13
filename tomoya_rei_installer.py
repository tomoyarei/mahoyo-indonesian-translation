from pathlib import Path
import shutil
import sys
import ctypes
import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox

if getattr(sys, "frozen", False):
    asset_dir = Path(sys._MEIPASS)
else:
    asset_dir = Path(__file__).resolve().parent

from mahoyo_tools import hfa


def copy_verified(source: Path, destination: Path) -> None:
    shutil.copy2(source, destination)
    if destination.stat().st_size != source.stat().st_size:
        raise IOError(f"Backup tidak lengkap: {destination.name}")


def hide_windows_path(path: Path) -> None:
    if sys.platform == "win32":
        ctypes.windll.kernel32.SetFileAttributesW(str(path), 0x02)


def find_game_folder() -> Path | None:
    candidates = [
        Path(r"C:\Program Files (x86)\Steam\steamapps\common\WITCH ON THE HOLY NIGHT"),
        Path(r"C:\Program Files\Steam\steamapps\common\WITCH ON THE HOLY NIGHT"),
    ]
    for folder in candidates:
        if (folder / "data00000.hfa").is_file():
            return folder
    return None


def install() -> None:
    folder = filedialog.askdirectory(title="Pilih folder game Witch on the Holy Night")
    if not folder:
        return
    game_dir = Path(folder)
    archive = game_dir / "data00000.hfa"
    image_0043 = asset_dir / "0043_title_bg1.png"
    image_0044 = asset_dir / "0044_title_bg2.png"
    translation_archive = asset_dir / "data00200.hfa"
    if not archive.is_file():
        messagebox.showerror("Tidak ditemukan", "Folder tersebut tidak memiliki data00000.hfa.")
        return
    if not image_0043.is_file() or not image_0044.is_file() or not translation_archive.is_file():
        messagebox.showerror("File mod kurang", "Data terjemahan dan kedua PNG harus dibundel bersama aplikasi.")
        return
    try:
        translation_target = game_dir / "data00200.hfa"
        backup_dir = game_dir / "TomoyaRei_Backup"
        backup_dir.mkdir(exist_ok=True)
        hide_windows_path(backup_dir)
        backup = backup_dir / "data00000.hfa.original"
        translation_backup = backup_dir / "data00200.hfa.original"
        if not backup.is_file():
            copy_verified(archive, backup)
            hide_windows_path(backup)
        if translation_target.is_file() and not translation_backup.is_file():
            copy_verified(translation_target, translation_backup)
            hide_windows_path(translation_backup)
        with hfa.HfaArchive(str(archive), "rw") as archive_file:
            archive_file["title_bg1.cbg"].inject(str(image_0043))
            archive_file["title_bg2.cbg"].inject(str(image_0044))
        shutil.copy2(translation_archive, translation_target)
        messagebox.showinfo("Berhasil", "Mod berhasil dipasang.")
    except Exception as error:
        messagebox.showerror("Pemasangan gagal", str(error))


def restore() -> None:
    folder = filedialog.askdirectory(title="Pilih folder game untuk memulihkan file asli")
    if not folder:
        return
    game_dir = Path(folder)
    backup_dir = game_dir / "TomoyaRei_Backup"
    available = {
        name: backup_dir / name
        for name in ("data00000.hfa.original", "data00200.hfa.original")
        if (backup_dir / name).is_file()
    }
    if not available:
        messagebox.showwarning("Backup tidak ditemukan", "Tidak ada backup mod ini di folder game tersebut.")
        return
    if not messagebox.askyesno("Konfirmasi pemulihan", "Kembalikan file game dari backup terbaru?"):
        return
    try:
        for name, backup in available.items():
            target_name = name.replace(".original", "")
            copy_verified(backup, game_dir / target_name)
        messagebox.showinfo("Berhasil", "File asli berhasil dipulihkan.")
    except Exception as error:
        messagebox.showerror("Pemulihan gagal", str(error))


root = tk.Tk()
root.title("Tomoya Rei | Pemasang Mod")
root.resizable(False, False)
tk.Label(root, text="WITCH ON THE HOLY NIGHT", font=("Segoe UI", 16, "bold"), padx=30).pack(pady=(18, 3))
tk.Label(root, text="Paket Bahasa Indonesia • Tomoya Rei", font=("Segoe UI", 10)).pack(pady=(0, 15))
tk.Label(root, text="Pilih folder instalasi game untuk memasang atau memulihkan mod.").pack(pady=(0, 10))
buttons = tk.Frame(root)
buttons.pack(pady=(0, 18))
tk.Button(buttons, text="PASANG MOD", command=install, width=22, padx=10, pady=8).grid(row=0, column=0, padx=5)
tk.Button(buttons, text="PULIHKAN FILE ASLI", command=restore, width=22, padx=10, pady=8).grid(row=0, column=1, padx=5)
detected = find_game_folder()
if detected:
    tk.Label(root, text=f"Lokasi Steam terdeteksi: {detected}", fg="#356859").pack(pady=(0, 12))
root.mainloop()
