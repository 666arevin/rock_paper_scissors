from pathlib import Path
import subprocess
import sys
import os
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent
start_path = BASE_DIR / "app"
messege = "Запустить игру?"

res = messagebox.askokcancel("Сообщение", messege)
if not res:
    messagebox.showinfo("Сообщение", "Отменено пользователем. CLI программа не будет запущена.")
    sys.exit()

subprocess.run([
        "powershell",
        "-NoExit",
        "-Command",
        f'cd "{start_path}"; python start.py -h;'
    ])