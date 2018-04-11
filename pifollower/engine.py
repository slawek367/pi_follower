from pifollower.config import Config
import RPi.GPIO as GPIO

class Engine():

    def __init__(self, engine_side):
        self.conf = Config()
        self.pin = {}
        self.pwm = None
        self.pwm_value = 0
        self.current_direction = "stop"
        self.initialize(engine_side)

    def initialize(self, engine_side):
        if engine_side == "left":
            print("set pins for left engine")
            self.pin['in_1'] = self.conf.pin["ain_1"]
            self.pin['in_2'] = self.conf.pin["ain_2"]
            self.pin['pwm'] = self.conf.pin["pwm_a"]
        elif engine_side == "right":
            self.pin['in_1'] = self.conf.pin["bin_1"]
            self.pin['in_2'] = self.conf.pin["bin_2"]
            self.pin['pwm'] = self.conf.pin["pwm_b"]
        else:
            pass

        GPIO.setup(self.pin['pwm'], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.pin['in_1'], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.pin['in_2'], GPIO.OUT, initial=GPIO.LOW)
        self.pwm = GPIO.PWM(self.pin['pwm'], self.conf.engine_frequency)

    def set_forward_direction(self):
        self.current_direction = "forward"
        GPIO.output(self.pin['in_1'], GPIO.LOW)
        GPIO.output(self.pin['in_2'], GPIO.HIGH)

    def set_backward_direction(self):
        self.current_direction = "backward"
        GPIO.output(self.pin['in_1'], GPIO.HIGH)
        GPIO.output(self.pin['in_2'], GPIO.LOW)

    def set_pwm(self, pwm_percent):
        self.pwm_value = pwm_percent
        self.pwm.ChangeDutyCycle(pwm_percent)

    def start(self):
        self.pwm.start(self.pwm_value)

    def stop(self):
        self.current_direction = "stop"
        GPIO.output(self.pin['in_1'], GPIO.LOW)
        GPIO.output(self.pin['in_2'], GPIO.LOW)
        self.pwm.stop()