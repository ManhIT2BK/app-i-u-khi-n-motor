import threading
import time


class WavePatterns:

    def __init__(self, modes):

        self.modes = modes

        self.running = False

    # ====================================
    # START PATTERN
    # ====================================

    def start_pattern(

        self,

        pattern_func,

        motors
    ):

        # tránh chạy nhiều pattern cùng lúc
        if self.running:

            return

        self.running = True

        threading.Thread(

            target=pattern_func,

            args=(motors,),

            daemon=True

        ).start()

    # ====================================
    # STOP PATTERN
    # ====================================

    def stop_pattern(

        self,

        motors
    ):

        self.running = False

        for motor in motors:

            self.modes.stop_motor(motor)

    # ====================================
    # SINE WAVE
    # ====================================

    def sine_wave(

        self,

        motors
    ):

        while self.running:

            # FORWARD

            for motor in motors:

                self.modes.constant_mode(

                    motor,

                    2,

                    "FORWARD"
                )

            time.sleep(2)

            # BACKWARD

            for motor in motors:

                self.modes.constant_mode(

                    motor,

                    2,

                    "BACKWARD"
                )

            time.sleep(2)

    # ====================================
    # TSUNAMI MODE
    # ====================================

    def tsunami_wave(

        self,

        motors
    ):

        while self.running:

            # hút nước

            for motor in motors:

                self.modes.constant_mode(

                    motor,

                    2,

                    "BACKWARD"
                )

            time.sleep(3)

            # đẩy mạnh

            for motor in motors:

                self.modes.ramp_up_mode(

                    motor,

                    3,

                    "FORWARD"
                )

            time.sleep(4)

    # ====================================
    # STANDING WAVE
    # ====================================

    def standing_wave(

        self,

        motors
    ):

        resonance_time = 1.2

        while self.running:

            # FORWARD

            for motor in motors:

                self.modes.constant_mode(

                    motor,

                    2,

                    "FORWARD"
                )

            time.sleep(resonance_time)

            # BACKWARD

            for motor in motors:

                self.modes.constant_mode(

                    motor,

                    2,

                    "BACKWARD"
                )

            time.sleep(resonance_time)