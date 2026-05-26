# khai báo cổng
SERIAL_PORT = 'COM10'
BAUD_RATE = 9600

CENTER_PWM = 1500
# maping tốc độ
LEVEL_MAP = {
    1:50,
    2:100,
    3:150
}

# Mapping từ số thứ tự Motor trên UI sang số Channel trên Arduino
MOTOR_TO_CHANNEL = {
    1: 5,
    2: 6,
    3: 4,
    4: 2,
    5: 1,
    6: 3
}