from config import Config
import RPi.GPIO as GPIO

class Engine():

    def __init__(self, engine_side):

        self.pwm_percent = 0
        self.pwm_value = 0
        self.current_direction = None
        self.initialize(engine_side)

    def initialize(self, engine_side):
        if engine_side == "left":
            GPIO.setup(p["AIN_1"], GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(p["AIN_2"], GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(p["BIN_1"], GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(p["BIN_2"], GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(p["PWM_a"], GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(p["PWM_b"], GPIO.OUT, initial=GPIO.HIGH)
        elif engine_side == "right":
            
        else:
            pass
        

    def forward(self, ):

    def backward():
