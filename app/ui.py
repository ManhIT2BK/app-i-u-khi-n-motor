# import tkinter as tk
#             command=self.constant_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="RAMP UP",
#             width=20,
#             command=self.ramp_up_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="RAMP DOWN",
#             width=20,
#             command=self.ramp_down_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="STOP",
#             width=20,
#             command=self.stop_motor
#         ).pack(pady=5)

#     def get_values(self):

#         return (
#             self.selected_motor.get(),
#             self.selected_level.get(),
#             self.selected_direction.get()
#         )

#     def constant_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.constant_mode(
#             motor,
#             level,
#             direction
#         )

#     def ramp_up_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.ramp_up_mode(
#             motor,
#             level,
#             direction
#         )

#     def ramp_down_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.ramp_down_mode(
#             motor,
#             level,
#             direction
#         )

#     def stop_motor(self):

#         motor = self.selected_motor.get()

#         self.modes.stop_motor(motor)
# import tkinter as tk

# from modes import MotorModes


# class App:

#     def __init__(self,root,serial_manager):

#         self.root = root

#         self.root.title("THRUSTER CONTROL")

#         self.root.geometry("400x500")

#         self.modes = MotorModes(serial_manager)

#         self.selected_motor = tk.IntVar(value=1)

#         self.selected_level = tk.IntVar(value=1)

#         self.selected_direction = tk.StringVar(value="FORWARD")

#         self.build_ui()

#     def build_ui(self):

#         title = tk.Label(
#             self.root,
#             text="THRUSTER CONTROL",
#             font=("Arial",20)
#         )

#         title.pack(pady=10)

#         # ---------------- MOTOR ----------------

#         motor_frame = tk.LabelFrame(
#             self.root,
#             text="SELECT MOTOR"
#         )

#         motor_frame.pack(pady=10)

#         tk.Radiobutton(
#             motor_frame,
#             text="MOTOR 1",
#             variable=self.selected_motor,
#             value=1
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             motor_frame,
#             text="MOTOR 2",
#             variable=self.selected_motor,
#             value=2
#         ).pack(anchor='w')

#         # ---------------- LEVEL ----------------

#         level_frame = tk.LabelFrame(
#             self.root,
#             text="LEVEL"
#         )

#         level_frame.pack(pady=10)

#         tk.Radiobutton(
#             level_frame,
#             text="LEVEL 1",
#             variable=self.selected_level,
#             value=1
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             level_frame,
#             text="LEVEL 2",
#             variable=self.selected_level,
#             value=2
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             level_frame,
#             text="LEVEL 3",
#             variable=self.selected_level,
#             value=3
#         ).pack(anchor='w')

#         # ---------------- DIRECTION ----------------

#         direction_frame = tk.LabelFrame(
#             self.root,
#             text="DIRECTION"
#         )

#         direction_frame.pack(pady=10)

#         tk.Radiobutton(
#             direction_frame,
#             text="FORWARD",
#             variable=self.selected_direction,
#             value="FORWARD"
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             direction_frame,
#             text="BACKWARD",
#             variable=self.selected_direction,
#             value="BACKWARD"
#         ).pack(anchor='w')

#         # ---------------- MODES ----------------

#         mode_frame = tk.LabelFrame(
#             self.root,
#             text="MODES"
#         )

#         mode_frame.pack(pady=10)

#         tk.Button(
#             mode_frame,
#             text="CONSTANT",
#             width=20,
#             command=self.constant_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="RAMP UP",
#             width=20,
#             command=self.ramp_up_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="RAMP DOWN",
#             width=20,
#             command=self.ramp_down_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="STOP",
#             width=20,
#             command=self.stop_motor
#         ).pack(pady=5)

#     def get_values(self):

#         return (
#             self.selected_motor.get(),
#             self.selected_level.get(),
#             self.selected_direction.get()
#         )

#     def constant_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.constant_mode(
#             motor,
#             level,
#             direction
#         )

#     def ramp_up_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.ramp_up_mode(
#             motor,
#             level,
#             direction
#         )

#     def ramp_down_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.ramp_down_mode(
#             motor,
#             level,
#             direction
#         )

#     def stop_motor(self):

#         motor = self.selected_motor.get()

#         self.modes.stop_motor(motor)
# import tkinter as tk

# from modes import MotorModes


# class App:

#     def __init__(self,root,serial_manager):

#         self.root = root

#         self.root.title("THRUSTER CONTROL")

#         self.root.geometry("400x500")

#         self.modes = MotorModes(serial_manager)

#         self.selected_motor = tk.IntVar(value=1)

#         self.selected_level = tk.IntVar(value=1)

#         self.selected_direction = tk.StringVar(value="FORWARD")

#         self.build_ui()

#     def build_ui(self):

#         title = tk.Label(
#             self.root,
#             text="THRUSTER CONTROL",
#             font=("Arial",20)
#         )

#         title.pack(pady=10)

#         # ---------------- MOTOR ----------------

#         motor_frame = tk.LabelFrame(
#             self.root,
#             text="SELECT MOTOR"
#         )

#         motor_frame.pack(pady=10)

#         tk.Radiobutton(
#             motor_frame,
#             text="MOTOR 1",
#             variable=self.selected_motor,
#             value=1
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             motor_frame,
#             text="MOTOR 2",
#             variable=self.selected_motor,
#             value=2
#         ).pack(anchor='w')

#         # ---------------- LEVEL ----------------

#         level_frame = tk.LabelFrame(
#             self.root,
#             text="LEVEL"
#         )

#         level_frame.pack(pady=10)

#         tk.Radiobutton(
#             level_frame,
#             text="LEVEL 1",
#             variable=self.selected_level,
#             value=1
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             level_frame,
#             text="LEVEL 2",
#             variable=self.selected_level,
#             value=2
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             level_frame,
#             text="LEVEL 3",
#             variable=self.selected_level,
#             value=3
#         ).pack(anchor='w')

#         # ---------------- DIRECTION ----------------

#         direction_frame = tk.LabelFrame(
#             self.root,
#             text="DIRECTION"
#         )

#         direction_frame.pack(pady=10)

#         tk.Radiobutton(
#             direction_frame,
#             text="FORWARD",
#             variable=self.selected_direction,
#             value="FORWARD"
#         ).pack(anchor='w')

#         tk.Radiobutton(
#             direction_frame,
#             text="BACKWARD",
#             variable=self.selected_direction,
#             value="BACKWARD"
#         ).pack(anchor='w')

#         # ---------------- MODES ----------------

#         mode_frame = tk.LabelFrame(
#             self.root,
#             text="MODES"
#         )

#         mode_frame.pack(pady=10)

#         tk.Button(
#             mode_frame,
#             text="CONSTANT",
#             width=20,
#             command=self.constant_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="RAMP UP",
#             width=20,
#             command=self.ramp_up_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="RAMP DOWN",
#             width=20,
#             command=self.ramp_down_mode
#         ).pack(pady=5)

#         tk.Button(
#             mode_frame,
#             text="STOP",
#             width=20,
#             command=self.stop_motor
#         ).pack(pady=5)

#     def get_values(self):

#         return (
#             self.selected_motor.get(),
#             self.selected_level.get(),
#             self.selected_direction.get()
#         )

#     def constant_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.constant_mode(
#             motor,
#             level,
#             direction
#         )

#     def ramp_up_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.ramp_up_mode(
#             motor,
#             level,
#             direction
#         )

#     def ramp_down_mode(self):

#         motor,level,direction = self.get_values()

#         self.modes.ramp_down_mode(
#             motor,
#             level,
#             direction
#         )

#     def stop_motor(self):

#         motor = self.selected_motor.get()

#         self.modes.stop_motor(motor)
import tkinter as tk

from modes import MotorModes


class App:

    def __init__(self,root,serial_manager):

        self.root = root

        self.root.title("THRUSTER CONTROL")

        self.root.geometry("400x500")

        self.modes = MotorModes(serial_manager)

        self.selected_motor = tk.IntVar(value=1)

        self.selected_level = tk.IntVar(value=1)

        self.selected_direction = tk.StringVar(value="FORWARD")

        self.build_ui()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="THRUSTER CONTROL",
            font=("Arial",20)
        )

        title.pack(pady=10)

        # MOTOR

        motor_frame = tk.LabelFrame(
            self.root,
            text="SELECT MOTOR"
        )

        motor_frame.pack(pady=10)

        tk.Radiobutton(
            motor_frame,
            text="MOTOR 1",
            variable=self.selected_motor,
            value=1
        ).pack(anchor='w')

        tk.Radiobutton(
            motor_frame,
            text="MOTOR 2",
            variable=self.selected_motor,
            value=2
        ).pack(anchor='w')

        # LEVEL

        level_frame = tk.LabelFrame(
            self.root,
            text="LEVEL"
        )

        level_frame.pack(pady=10)

        tk.Radiobutton(
            level_frame,
            text="LEVEL 1",
            variable=self.selected_level,
            value=1
        ).pack(anchor='w')

        tk.Radiobutton(
            level_frame,
            text="LEVEL 2",
            variable=self.selected_level,
            value=2
        ).pack(anchor='w')

        tk.Radiobutton(
            level_frame,
            text="LEVEL 3",
            variable=self.selected_level,
            value=3
        ).pack(anchor='w')

        # DIRECTION

        direction_frame = tk.LabelFrame(
            self.root,
            text="DIRECTION"
        )

        direction_frame.pack(pady=10)

        tk.Radiobutton(
            direction_frame,
            text="FORWARD",
            variable=self.selected_direction,
            value="FORWARD"
        ).pack(anchor='w')

        tk.Radiobutton(
            direction_frame,
            text="BACKWARD",
            variable=self.selected_direction,
            value="BACKWARD"
        ).pack(anchor='w')

        # MODES

        mode_frame = tk.LabelFrame(
            self.root,
            text="MODES"
        )

        mode_frame.pack(pady=10)

        tk.Button(
            mode_frame,
            text="CONSTANT",
            width=20,
            command=self.constant_mode
        ).pack(pady=5)

        tk.Button(
            mode_frame,
            text="RAMP UP",
            width=20,
            command=self.ramp_up_mode
        ).pack(pady=5)

        tk.Button(
            mode_frame,
            text="RAMP DOWN",
            width=20,
            command=self.ramp_down_mode
        ).pack(pady=5)

        tk.Button(
            mode_frame,
            text="STOP",
            width=20,
            command=self.stop_motor
        ).pack(pady=5)

    def get_values(self):

        return (
            self.selected_motor.get(),
            self.selected_level.get(),
            self.selected_direction.get()
        )

    def constant_mode(self):

        motor,level,direction = self.get_values()

        self.modes.constant_mode(
            motor,
            level,
            direction
        )

    def ramp_up_mode(self):

        motor,level,direction = self.get_values()

        self.modes.ramp_up_mode(
            motor,
            level,
            direction
        )

    def ramp_down_mode(self):

        motor,level,direction = self.get_values()

        self.modes.ramp_down_mode(
            motor,
            level,
            direction
        )

    def stop_motor(self):

        motor = self.selected_motor.get()

        self.modes.stop_motor(motor)