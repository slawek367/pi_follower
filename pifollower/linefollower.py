import RPi.GPIO as GPIO
from pifollower.config import Config
from pifollower.engine import Engine
from sensors import Sensors
from time import sleep

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

def test_right_engine():
    print("Start right engine")
    engine_right = Engine("right")
    engine_right.set_forward_direction()
    engine_right.set_pwm(50)
    engine_right.start()
    sleep(1)
    engine_right.set_backward_direction()
    sleep(1)
    print("Stop right engine")
    engine_right.stop() 

def test_pwm():
    engine_left = Engine("left")
    engine_right = Engine("right")
    engine_left.set_forward_direction()
    engine_right.set_forward_direction()
    engine_left.set_pwm(50)
    engine_right.set_pwm(50)
    engine_left.start()
    engine_right.start()

    for y in range(5):
        for x in range(10, 100):
            engine_left.set_pwm(x)
            engine_right.set_pwm(x)
            sleep(0.01)
        for x in range(100, 10, -1):
            engine_left.set_pwm(x)
            engine_right.set_pwm(x)
            sleep(0.003)  
    engine_left.stop()
    engine_right.stop()

def ride_keyboard():
    engine_left = Engine("left")
    engine_right = Engine("right")

def main():
    GPIO.setmode(GPIO.BOARD) #refference by pin number
    GPIO.setwarnings(False)
    #test_left_engine()
    #test_right_engine()
    #test_pwm()
    sensors = Sensors()
    while True:
        print(sensors.check_sensors_state())
        sleep(0.5)
        pass
    
    GPIO.cleanup()

main()

'''
TODO
po I2c wyswietlacz oLED, BS1 przelutowac do gory
    pin3 - SDA
    pin5 - SCL
czujnik temperatury i wilgotnosci DHT11, 1wire magistrala
    pin8
czujnik temperatury DS18B20, 1wire magistrala
    pin37
WS2811 - 2 w szeregu spiete
    pin10
'''

