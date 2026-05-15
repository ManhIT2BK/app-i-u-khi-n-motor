# import threading
# import time

# CENTER_PWM = 1500

# class MotorModes:

#     def __init__(self,serial_manager):

#         self.serial = serial_manager

#     def compute_pwm(self,level,direction):# tính pwm dựa vào level và direction

#         if level == 1:
#             offset = 50

#         elif level == 2:
#             offset = 100

#         else:
#             offset = 150

#         if direction == "FORWARD":

#             return CENTER_PWM + offset

#         else:

#             return CENTER_PWM - offset

#     def ramp_up_mode(self,motor,level,direction):#tăng tốc dần từ 1500 sang 2 mốc 2 bên

#         threading.Thread(
#             target=self._ramp_up,
#             args=(motor,level,direction),
#             daemon=True
#         ).start()

#     def _ramp_up(self,motor,level,direction):

#         target = self.compute_pwm(level,direction)

#         step = 10

#         if target > CENTER_PWM:

#             for pwm in range(CENTER_PWM,target+1,step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#         else:

#             for pwm in range(CENTER_PWM,target-1,-step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#     def ramp_down_mode(self,motor,level,direction):#giảm tốc dần về stop

#         threading.Thread(
#             target=self._ramp_down,
#             args=(motor,level,direction),
#             daemon=True
#         ).start()

#     def _ramp_down(self,motor,level,direction):

#         start_pwm = self.compute_pwm(level,direction)#PWM hiện tại của motor

#         step = 10

#         if start_pwm > CENTER_PWM:

#             for pwm in range(start_pwm,CENTER_PWM-1,-step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#         else:

#             for pwm in range(start_pwm,CENTER_PWM+1,step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#     def stop_motor(self,motor):

#         self.serial.send_pwm(motor,CENTER_PWM)
# import threading
# import time

# CENTER_PWM = 1500


# class MotorModes:

#     def __init__(self,serial_manager):

#         self.serial = serial_manager

#     def compute_pwm(self,level,direction):

#         if level == 1:
#             offset = 50

#         elif level == 2:
#             offset = 100

#         else:
#             offset = 150

#         if direction == "FORWARD":

#             return CENTER_PWM + offset

#         else:

#             return CENTER_PWM - offset

#     def constant_mode(self,motor,level,direction):

#         pwm = self.compute_pwm(level,direction)

#         self.serial.send_pwm(motor,pwm)

#     def ramp_up_mode(self,motor,level,direction):

#         threading.Thread(
#             target=self._ramp_up,
#             args=(motor,level,direction),
#             daemon=True
#         ).start()

#     def _ramp_up(self,motor,level,direction):

#         target = self.compute_pwm(level,direction)

#         step = 10

#         if target > CENTER_PWM:

#             for pwm in range(CENTER_PWM,target+1,step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#         else:

#             for pwm in range(CENTER_PWM,target-1,-step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#     def ramp_down_mode(self,motor,level,direction):

#         threading.Thread(
#             target=self._ramp_down,
#             args=(motor,level,direction),
#             daemon=True
#         ).start()

#     def _ramp_down(self,motor,level,direction):

#         start_pwm = self.compute_pwm(level,direction)

#         step = 10

#         if start_pwm > CENTER_PWM:

#             for pwm in range(start_pwm,CENTER_PWM-1,-step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#         else:

#             for pwm in range(start_pwm,CENTER_PWM+1,step):

#                 self.serial.send_pwm(motor,pwm)

#                 time.sleep(0.05)

#     def stop_motor(self,motor):

#         self.serial.send_pwm(motor,CENTER_PWM)
import threading
import time

CENTER_PWM = 1500


class MotorModes:

    def __init__(self,serial_manager):

        self.serial = serial_manager

    def compute_pwm(self,level,direction):

        if level == 1:
            offset = 50

        elif level == 2:
            offset = 100

        else:
            offset = 150

        if direction == "FORWARD":

            return CENTER_PWM + offset

        else:

            return CENTER_PWM - offset

    def constant_mode(self,motor,level,direction):

        pwm = self.compute_pwm(level,direction)

        self.serial.send_pwm(motor,pwm)

    def ramp_up_mode(self,motor,level,direction):

        threading.Thread(
            target=self._ramp_up,
            args=(motor,level,direction),
            daemon=True
        ).start()

    def _ramp_up(self,motor,level,direction):

        target = self.compute_pwm(level,direction)

        step = 10

        if target > CENTER_PWM:

            for pwm in range(CENTER_PWM,target+1,step):

                self.serial.send_pwm(motor,pwm)

                time.sleep(0.05)

        else:

            for pwm in range(CENTER_PWM,target-1,-step):

                self.serial.send_pwm(motor,pwm)

                time.sleep(0.05)

    def ramp_down_mode(self,motor,level,direction):

        threading.Thread(
            target=self._ramp_down,
            args=(motor,level,direction),
            daemon=True
        ).start()

    def _ramp_down(self,motor,level,direction):

        start_pwm = self.compute_pwm(level,direction)

        step = 10

        if start_pwm > CENTER_PWM:

            for pwm in range(start_pwm,CENTER_PWM-1,-step):

                self.serial.send_pwm(motor,pwm)

                time.sleep(0.05)

        else:

            for pwm in range(start_pwm,CENTER_PWM+1,step):

                self.serial.send_pwm(motor,pwm)

                time.sleep(0.05)

    def stop_motor(self,motor):

        self.serial.send_pwm(motor,CENTER_PWM)