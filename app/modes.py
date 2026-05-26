import threading
import time
from config import LEVEL_MAP

CENTER_PWM = 1500

# =====================================
# MOTOR ĐẢO CHIỀU PWM
# để tạo cùng hướng dòng nước
# =====================================

REVERSED_MOTORS = [2, 4]


class MotorModes:

    def __init__(self, serial_manager):

        self.serial = serial_manager

        # =================================
        # PWM HIỆN TẠI CỦA MOTOR
        # =================================

        self.current_pwm = {

            i: CENTER_PWM

            for i in range(1, 7)
        }

    # =====================================
    # TÍNH PWM
    # =====================================

    def compute_pwm(

        self,

        motor,

        level,

        direction
    ):

        # =================================
        # SPEED LEVEL
        # =================================

        # Sử dụng giá trị từ file config thay vì fix cứng
        offset = LEVEL_MAP.get(level, 50)

        # =================================
        # MOTOR CÓ BỊ ĐẢO KHÔNG
        # =================================

        reverse = motor in REVERSED_MOTORS

        print(

            f"MOTOR {motor} | REVERSED = {reverse}"
        )

        # =================================
        # FORWARD
        # =================================

        if direction == "FORWARD":

            if reverse:

                pwm = CENTER_PWM - offset

            else:

                pwm = CENTER_PWM + offset

        # =================================
        # BACKWARD
        # =================================

        else:

            if reverse:

                pwm = CENTER_PWM + offset

            else:

                pwm = CENTER_PWM - offset

        print(

            f"MOTOR {motor} PWM = {pwm}"
        )

        return pwm

    # =====================================
    # CONSTANT MODE
    # =====================================

    def constant_mode(

        self,

        motor,

        level,

        direction
    ):

        pwm = self.compute_pwm(

            motor,

            level,

            direction
        )

        self.serial.send_pwm(

            motor,

            pwm
        )

        self.current_pwm[motor] = pwm

    # =====================================
    # RAMP UP MODE
    # =====================================

    def ramp_up_mode(

        self,

        motor,

        level,

        direction
    ):

        threading.Thread(

            target=self._ramp_up,

            args=(motor, level, direction),

            daemon=True

        ).start()

    def _ramp_up(

        self,

        motor,

        level,

        direction
    ):

        target = self.compute_pwm(

            motor,

            level,

            direction
        )

        start_pwm = self.current_pwm[motor]

        step = 5

        # =================================
        # TĂNG PWM
        # =================================

        if target > start_pwm:

            for pwm in range(

                start_pwm,

                target + 1,

                step
            ):

                self.serial.send_pwm(

                    motor,

                    pwm
                )

                self.current_pwm[motor] = pwm

                time.sleep(0.1)

        # =================================
        # GIẢM PWM
        # =================================

        else:

            for pwm in range(

                start_pwm,

                target - 1,

                -step
            ):

                self.serial.send_pwm(

                    motor,

                    pwm
                )

                self.current_pwm[motor] = pwm

                time.sleep(0.1)

    # =====================================
    # RAMP DOWN MODE
    # =====================================

    def ramp_down_mode(

        self,

        motor
    ):

        threading.Thread(

            target=self._ramp_down,

            args=(motor,),

            daemon=True

        ).start()

    def _ramp_down(

        self,

        motor
    ):

        start_pwm = self.current_pwm[motor]

        step = 5

        # =================================
        # GIẢM VỀ 1500
        # =================================

        if start_pwm > CENTER_PWM:

            for pwm in range(

                start_pwm,

                CENTER_PWM - 1,

                -step
            ):

                self.serial.send_pwm(

                    motor,

                    pwm
                )

                self.current_pwm[motor] = pwm

                time.sleep(0.1)

        else:

            for pwm in range(

                start_pwm,

                CENTER_PWM + 1,

                step
            ):

                self.serial.send_pwm(

                    motor,

                    pwm
                )

                self.current_pwm[motor] = pwm

                time.sleep(0.1)

    # =====================================
    # STOP MOTOR
    # =====================================

    def stop_motor(

        self,

        motor
    ):

        self.serial.send_pwm(

            motor,

            CENTER_PWM
        )

        self.current_pwm[motor] = CENTER_PWM