import RPi.GPIO as GPIO
from config import Config
from engine import Engine

def set_sensors(sensors):
    GPIO.setup(sensors, GPIO.IN)

def check_sensors_state(sensors):
    sensors_state = []
    for sensor in sensors:
        if GPIO.input(sensor):
            sensors_state.append("- ")
        else:
            sensors_state.append("+ ")
    return sensors_state

def main():
    GPIO.setmode(GPIO.BOARD) #refference by pin number
    GPIO.setwarnings(False)

    while True:
        pass
    
    GPIO.cleanup()

main()

'''
sensors = [7, 11, 15, 13, 21, 19, 21, 23, 31, 29, 33, 35] #od lewej do prawej
set_sensors(sensors)

while True:
    for x in check_sensors_state(sensors):
        sys.stdout.write(x)
    print("\n")
    sleep(0.2)

GPIO.setup(p["AIN_1"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(p["AIN_2"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["BIN_1"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(p["BIN_2"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["PWM_a"], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(p["PWM_b"], GPIO.OUT, initial=GPIO.HIGH)
sleep(3)
GPIO.cleanup()
'''