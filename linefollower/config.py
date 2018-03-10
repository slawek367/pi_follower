class Config():

    def __init__(self):
        self.pin = {
            "pwm_a": 12,  # left engine
            "pwm_b": 32,  # right engine
            "ain_1": 24,  # left engine direction
            "ain_2": 22,  # left engine direction
            "bin_1": 26,  # right engine direction
            "bin_2": 38,  # right engine direction
            "led_left": 16,  # left led
            "led_sensor": 40,  # sensor led
            "switch_left": 18,
            "switch_right": 36
        }
        self.engine_frequency = 1000#in hz