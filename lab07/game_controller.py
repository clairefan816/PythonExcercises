import pair_of_dice


class GameController:

    def __init__(self):
        self.pod = pair_of_dice.PairOfDice()
        self.point = 0

    # returns False if the game ended, otherwise True.
    def play(self):
        print()
        input("Please enter to roll the dice...")
        self.pod.roll_dice()
        print(f"You rolled {self.pod.current_value()}. ", end='')
        # First round.
        if self.point == 0:
            if self.pod.current_value() in [2, 3, 12]:
                print('You lost.')
                return False
            elif self.pod.current_value() in [7, 11]:
                print('You win!')
                return False
            else:
                self.point = self.pod.current_value()
                return True
        # Other round.
        else:
            if self.pod.current_value() == 7:
                print('You lost.')
                return False
            elif self.pod.current_value() == self.point:
                print('You win!')
                return False
            else:
                return True
