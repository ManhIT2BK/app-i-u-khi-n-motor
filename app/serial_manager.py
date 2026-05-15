
# import serial
# import time


# class SerialManager:

#     def __init__(self,port,baudrate):

#         self.arduino = serial.Serial(
#             port,
#             baudrate,
#             timeout=1
#         )

#         time.sleep(2)

#     def send_pwm(self,motor,pwm):

#         message = f"{motor},{pwm}\n"

#         print("SEND:",message)

#         self.arduino.write(message.encode())
import serial
import time


class SerialManager:

    def __init__(self,port,baudrate):

        self.arduino = serial.Serial(
            port,
            baudrate,
            timeout=1
        )

        time.sleep(2)

        print("ARDUINO CONNECTED")

    def send_pwm(self,motor,pwm):

        message = f"{motor},{pwm}\n"

        print("SEND:",message)

        self.arduino.write(message.encode())