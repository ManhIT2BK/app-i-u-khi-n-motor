import tkinter as tk

from modes import MotorModes
from patterns import WavePatterns


class App:

    def __init__(self, root, serial_manager):

        self.root = root

        self.root.title("THRUSTER CONTROL")
        print("NEW UI LOADED")

        self.root.geometry("650x1400")

        self.modes = MotorModes(serial_manager)

        self.patterns = WavePatterns(self.modes)

        # =================================
        # MOTOR CHECKBUTTONS
        # =================================

        self.motor_vars = {

            i: tk.IntVar()

            for i in range(1, 7)
        }

        # =================================
        # LEVEL + DIRECTION
        # =================================

        self.selected_level = tk.IntVar(value=1)

        self.selected_direction = tk.StringVar(
            value="FORWARD"
        )

        # build UI
        self.build_ui()

    # =====================================
    # BUILD UI
    # =====================================

    def build_ui(self):

        # =================================
        # TITLE
        # =================================

        title = tk.Label(

            self.root,

            text="THRUSTER CONTROL PANEL",

            font=("Arial", 20)

        )

        title.pack(pady=10)

        # =================================
        # MOTOR FRAME
        # =================================

        motor_frame = tk.LabelFrame(

            self.root,

            text="SELECT MOTORS",

            padx=10,

            pady=10
        )

        motor_frame.pack(

            pady=10,

            fill="x",

            padx=20
        )

        for i in range(1, 7):

            tk.Checkbutton(

                motor_frame,

                text=f"MOTOR {i}",

                variable=self.motor_vars[i]

            ).pack(anchor='w')

        # =================================
        # LEVEL FRAME
        # =================================

        level_frame = tk.LabelFrame(

            self.root,

            text="SELECT SPEED LEVEL",

            padx=10,

            pady=10
        )

        level_frame.pack(

            pady=10,

            fill="x",

            padx=20
        )

        for i in range(1, 4):

            tk.Radiobutton(

                level_frame,

                text=f"LEVEL {i}",

                variable=self.selected_level,

                value=i

            ).pack(anchor='w')

        # =================================
        # DIRECTION FRAME
        # =================================

        direction_frame = tk.LabelFrame(

            self.root,

            text="SELECT DIRECTION",

            padx=10,

            pady=10
        )

        direction_frame.pack(

            pady=10,

            fill="x",

            padx=20
        )

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

        # =================================
        # MANUAL CONTROL FRAME
        # =================================

        mode_frame = tk.LabelFrame(

            self.root,

            text="MANUAL CONTROL",

            padx=10,

            pady=10
        )

        mode_frame.pack(

            pady=10,

            fill="x",

            padx=20
        )

        # CONSTANT

        tk.Button(

            mode_frame,

            text="CONSTANT MODE",

            width=25,

            height=2,

            command=self.constant_mode

        ).pack(pady=5)

        # RAMP UP

        tk.Button(

            mode_frame,

            text="RAMP UP",

            width=25,

            height=2,

            command=self.ramp_up_mode

        ).pack(pady=5)

        # RAMP DOWN

        tk.Button(

            mode_frame,

            text="RAMP DOWN",

            width=25,

            height=2,

            command=self.ramp_down_mode

        ).pack(pady=5)

        # STOP

        tk.Button(

            mode_frame,

            text="STOP MOTOR",

            width=25,

            height=2,

            command=self.stop_motor

        ).pack(pady=5)

        # =================================
        # WAVE PATTERNS FRAME
        # =================================

        pattern_frame = tk.LabelFrame(

            self.root,

            text="WAVE PATTERNS",

            padx=10,

            pady=10
        )

        pattern_frame.pack(

            pady=10,

            fill="x",

            padx=20
        )

        # SINE WAVE

        tk.Button(

            pattern_frame,

            text="SINE WAVE",

            width=25,

            height=2,

            command=self.sine_wave

        ).pack(pady=5)

        # TSUNAMI

        tk.Button(

            pattern_frame,

            text="TSUNAMI MODE",

            width=25,

            height=2,

            command=self.tsunami_wave

        ).pack(pady=5)

        # STANDING WAVE

        tk.Button(

            pattern_frame,

            text="STANDING WAVE",

            width=25,

            height=2,

            command=self.standing_wave

        ).pack(pady=5)

        # STOP PATTERN

        tk.Button(

            pattern_frame,

            text="STOP PATTERN",

            width=25,

            height=2,

            command=self.stop_pattern

        ).pack(pady=5)

    # =====================================
    # GET SELECTED MOTORS
    # =====================================

    def get_selected_motors(self):

        motors = []

        for motor, var in self.motor_vars.items():

            if var.get() == 1:

                motors.append(motor)

        return motors

    # =====================================
    # MANUAL MODES
    # =====================================

    def constant_mode(self):

        motors = self.get_selected_motors()

        level = self.selected_level.get()

        direction = self.selected_direction.get()

        for motor in motors:

            self.modes.constant_mode(

                motor,

                level,

                direction
            )

    def ramp_up_mode(self):

        motors = self.get_selected_motors()

        level = self.selected_level.get()

        direction = self.selected_direction.get()

        for motor in motors:

            self.modes.ramp_up_mode(

                motor,

                level,

                direction
            )

    def ramp_down_mode(self):

        motors = self.get_selected_motors()

        for motor in motors:

            self.modes.ramp_down_mode(motor)

    def stop_motor(self):

        motors = self.get_selected_motors()

        for motor in motors:

            self.modes.stop_motor(motor)

    # =====================================
    # PATTERN MODES
    # =====================================

    def sine_wave(self):

        motors = self.get_selected_motors()

        self.patterns.start_pattern(

            self.patterns.sine_wave,

            motors
        )

    def tsunami_wave(self):

        motors = self.get_selected_motors()

        self.patterns.start_pattern(

            self.patterns.tsunami_wave,

            motors
        )

    def standing_wave(self):

        motors = self.get_selected_motors()

        self.patterns.start_pattern(

            self.patterns.standing_wave,

            motors
        )

    def stop_pattern(self):

        motors = self.get_selected_motors()

        self.patterns.stop_pattern(

            motors
        )