import pytest
from linefollower.config import Config
from linefollower.engine import Engine
from linefollower.time import sleep

class TestClass(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD) #refference by pin number
        GPIO.setwarnings(False)
    
    def test_left_engine():
        print("Start left engine")
        engine_left = Engine("left")
        engine_left.set_forward_direction()
        engine_left.set_pwm(50)
        engine_left.start()
        sleep(1)
        engine_left.set_backward_direction()
        sleep(1)
        print("Stop left engine")
        engine_left.stop()