import random


class Die:
    def __init__(self):
        self.current_value = 0

    def roll(self):
        RANGE_LOW = 1
        RANGE_HIGH = 6
        self.current_value = random.randint(RANGE_LOW, RANGE_HIGH)
