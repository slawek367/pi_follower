import RPi.GPIO as GPIO
from pifollower.config import Config

class Sensors():
    
    def __init__(self):
        #self.sensors = [7, 11, 15, 13, 21, 19, 21, 23, 31, 29, 33, 35] #from left to right
        self.sensors = [7, 11, 15, 21, 19, 21, 23, 29, 33, 35] #from left to right, currently 2 sensors not work
        self.sensors_count = len(self.sensors)
        self.set_sensors()

    def set_sensors(self):
        GPIO.setup(self.sensors, GPIO.IN)

    # True - sesor is active
    def check_sensors_state(self):
        sensors_state = []
        for sensor in self.sensors:
            if GPIO.input(sensor):
                sensors_state.append(False)
            else:
                sensors_state.append(True)
        return sensors_state