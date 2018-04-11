import RPi.GPIO as GPIO
from pifollower.config import Config
from pifollower.engine import Engine
from pifollower.sensors import Sensors
from time import sleep
import threading

GPIO.setmode(GPIO.BOARD) #refference by pin number
GPIO.setwarnings(False)
COUNTER = 0

SENSORS_DATA = []
SENSORS_WEIGHT = [-30, -25, -18, -13, -4, 4, 13, 18, 25, 30]
PERV_ERR = 0
LINE_STREAKED = 0
ERROR = 0
PREVIOUS_ERROR = 0
KP = 3
KD = 15
MAX_PWM_PERCENT = 15

SENSORS = Sensors()
ENGINE_LEFT = Engine("left")
ENGINE_RIGHT = Engine("right")

def calculate_error():
    global PREVIOUS_ERROR
    global ERROR

    count = 0
    error = 0

    sensors_state = SENSORS.check_sensors_state()
    #print(sensors_state)

    for x in range(0, SENSORS.sensors_count):
        error += sensors_state[x] * SENSORS_WEIGHT[x]
        count += sensors_state[x]
    
    if not count == 0:
        error = error/count
        ERROR = error
        PREVIOUS_ERROR = ERROR
    else:
        ERROR = PREVIOUS_ERROR
    
    return ERROR

def pd():
    global ERROR
    global PREVIOUS_ERROR
    rozniczka = ERROR - PREVIOUS_ERROR
    PREVIOUS_ERROR = ERROR
    return KP*ERROR + KD*rozniczka

def set_pwm(right_engine_pwm, left_engine_pwm):
    if left_engine_pwm >= 0:
        if left_engine_pwm > 50:
            ENGINE_LEFT.set_pwm(50)
        else:
            ENGINE_LEFT.set_pwm(left_engine_pwm)
        ENGINE_LEFT.set_forward_direction()
    else:
        if left_engine_pwm < -50:
                ENGINE_LEFT.set_pwm(50)
        else:
            ENGINE_LEFT.set_pwm(left_engine_pwm*-1)
        ENGINE_LEFT.set_backward_direction()
        
    if right_engine_pwm >= 0:
        if right_engine_pwm > 50:
            ENGINE_RIGHT.set_pwm(50)
        else:
            ENGINE_RIGHT.set_pwm(right_engine_pwm)
        ENGINE_RIGHT.set_forward_direction()
    else:
        if right_engine_pwm < -50:
                ENGINE_RIGHT.set_pwm(50)
        else:
            ENGINE_RIGHT.set_pwm(right_engine_pwm*-1)
        ENGINE_RIGHT.set_backward_direction()

def loop():
    global COUNTER
    if COUNTER < 250:
        threading.Timer(0.002, loop).start()
    else:
        ENGINE_LEFT.stop()
        ENGINE_RIGHT.stop()

    error = calculate_error()
    regulation = pd()
    #print("LEFT: %s\tRIGHT: %s" %(MAX_PWM_PERCENT+regulation, MAX_PWM_PERCENT-regulation))
    set_pwm(MAX_PWM_PERCENT+regulation, MAX_PWM_PERCENT-regulation)
    COUNTER = COUNTER + 1

def initialize():
    ENGINE_LEFT.set_forward_direction()
    ENGINE_RIGHT.set_forward_direction()
    ENGINE_LEFT.set_pwm(MAX_PWM_PERCENT-15)
    ENGINE_RIGHT.set_pwm(MAX_PWM_PERCENT-15)
    ENGINE_LEFT.start()
    ENGINE_RIGHT.start()

initialize()
loop()

while True:
    pass