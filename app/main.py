import tkinter as tk # thư viện tkinter

from serial_manager import SerialManager # import lớp SerialManager từ serial_manager.py
from ui import App # import lớp App từ ui.py (giao diện người dùng)
import config

serial_manager = SerialManager(
    port='COM10',
    baudrate=9600
) # 

root = tk.Tk()# tạo cửa sổ chính

app = App(root,serial_manager)

root.mainloop() # chạy liên tục để bắt sự kiện