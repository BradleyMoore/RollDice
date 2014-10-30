from random import randint
from sys import argv, exit


def get_cl_args():
    """Call 2 cl arguments and return tuple."""
    num_of_dice = argv[1]
    sides_per_die = argv[2]

    dice = (num_of_dice, sides_per_die)
    return dice


def roll(die):
    """Input int and return int."""
    roll = randint(1, die)

    return roll


def restart():
    """Determine whether to exit or not."""
    quit = raw_input('Enter to roll again, type exit to quit.\n>')
    if quit == exit:
        sys.exit()
    elif quit == '':
        pass
    else:
        print '\n'
        restart()


def main(num_of_die):
    pass


while __name__ == '__main__':
    pass

