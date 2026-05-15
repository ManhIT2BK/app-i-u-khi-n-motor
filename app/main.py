# import tkinter as tk

# from serial_manager import SerialManager
# from ui import App

# serial_manager = SerialManager()

# root = tk.Tk()

# app = App(root,serial_manager)

# root.mainloop()
# import tkinter as tk

# from serial_manager import SerialManager
# from ui import App

# serial_manager = SerialManager(
#     port='COM5',
#     baudrate=9600
# )

# root = tk.Tk()

# app = App(root,serial_manager)

# root.mainloop()
# import tkinter as tk

# from serial_manager import SerialManager
# from ui import App

# print("START")

# serial_manager = SerialManager(
#     port='COM5',
#     baudrate=9600
# )

# print("SERIAL OK")

# root = tk.Tk()

# print("TK OK")

# app = App(root,serial_manager)

# print("APP OK")

# root.mainloop()
import tkinter as tk

from serial_manager import SerialManager
from ui import App

serial_manager = SerialManager(
    port='COM5',
    baudrate=9600
)

root = tk.Tk()

app = App(root,serial_manager)

root.mainloop()