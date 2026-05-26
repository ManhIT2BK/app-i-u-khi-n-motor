# Kết nối Arduino khi khởi tạo
# Gửi lệnh PWM cho motor theo định dạng motor_id,pwm_value

import serial 
import time
from config import MOTOR_TO_CHANNEL


class SerialManager:

    def __init__(self,port,baudrate):

        self.arduino = serial.Serial(
            port,
            baudrate,
            timeout=1
        )#serial.Serial(...): Mở cổng Serial (UART) kết nối với Arduino
        #lưu kết nối vào self.arduino để sử dụng

        time.sleep(2)

        print("ARDUINO CONNECTED")

    def send_pwm(self,motor,pwm):

        channel = MOTOR_TO_CHANNEL.get(motor, motor)
        message = f"{channel},{pwm}\n"

        print("SEND:",message)

        self.arduino.write(message.encode())