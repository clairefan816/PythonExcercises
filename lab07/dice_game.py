import game_controller


def main():
    print('---------------------------------------------')
    print('Welcome to street craps!')
    print()
    print("""
    Rules:
    If you roll 7 or 11 on your first roll, you win.
    If you roll 2, 3, or 12 on your first role, you lose.
    If you roll anything else, that's your 'point', and
    you keep rolling until you either roll your point
    again (win) or roll a 7 (lose)
    """)

    gc = game_controller.GameController()

    while True:
        if(not gc.play()):
            break


main()
