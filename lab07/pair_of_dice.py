import die


class PairOfDice:

    def __init__(self):
        self.die_one = die.Die()
        self.die_two = die.Die()

    def roll_dice(self):
        self.die_one.roll()
        self.die_two.roll()

    def current_value(self):
        die1_value = self.die_one.current_value
        die2_value = self.die_two.current_value
        return die1_value + die2_value
