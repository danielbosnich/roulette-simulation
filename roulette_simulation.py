"""
Simulation of the Roulette Martingale Strategy
"""

import logging
import random
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Board constants
GREEN = 'Green'
BLACK = 'Black'
RED = 'Red'
POCKETS = {
    0: GREEN,
    1: RED,
    2: BLACK,
    3: RED,
    4: BLACK,
    5: RED,
    6: BLACK,
    7: RED,
    8: BLACK,
    9: RED,
    10: BLACK,
    11: BLACK,
    12: RED,
    13: BLACK,
    14: RED,
    15: BLACK,
    16: RED,
    17: BLACK,
    18: RED,
    19: RED,
    20: BLACK,
    21: RED,
    22: BLACK,
    23: RED,
    24: BLACK,
    25: RED,
    26: BLACK,
    27: RED,
    28: BLACK,
    29: BLACK,
    30: RED,
    31: BLACK,
    32: RED,
    33: BLACK,
    34: RED,
    35: BLACK,
    36: RED
}


def main():
    """Run the Roulette simulation"""
    # Simulation variables
    num_plays = 10_000
    num_bets = 25  # Number of bets per play
    bank_start = 500
    starting_bet_size = 2
    bet_size_limit = 100  # Max bet size in Colorado
    wins = 0
    ending_bank_amounts = []

    # Start up logging
    logging.basicConfig(format='[%(asctime)s] %(levelname)s : %(message)s',
                        level=logging.INFO)

    # Simulation start time
    start_time = time.time()

    # Run the simulation
    for i in range(num_plays):
        # Reset the bank and the bet size
        current_bank = bank_start
        bet_size = starting_bet_size

        for j in range(num_bets):
            logging.debug('Placing bet # %i in simulation # %i', j, i)

            # Subtract money for the bet (only if there's enough)
            if current_bank-bet_size < 0:
                break
            current_bank -= bet_size

            # Simulate a single run of the game
            winning_pocket = random.randint(0, 36)
            winning_color = POCKETS[winning_pocket]
            logging.debug('The winning pocket is  %s', winning_pocket)
            logging.debug('The winning color is %s', winning_color)

            # Check if the bet won
            if winning_color == RED:
                current_bank = current_bank + bet_size * 2
                bet_size = starting_bet_size
                logging.debug('Won. The bank amount is now: %i', current_bank)
            else:
                bet_size *= 2
                if bet_size > bet_size_limit:
                    bet_size = starting_bet_size
                logging.debug('Lost. The bank amount is now: %i', current_bank)

        # Check if we made money or lost money and add bank amount to the list
        if current_bank > bank_start:
            wins += 1
        ending_bank_amounts.append(current_bank)

    # Figure out how many times we made money
    logging.info('We made money %.3f percent of the times we played',
                 wins/num_plays * 100)

    # Calculate simulation execution time
    logging.debug('It took the program %.3f seconds to run',
                  time.time()-start_time)

    # Create the histogram
    y_axis_weights = [1/len(ending_bank_amounts)] * len(ending_bank_amounts)
    plt.hist(ending_bank_amounts, bins=75, weights=y_axis_weights)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.xlabel('Ending bank amount ($)')
    plt.ylabel('Frequency')
    plt.title('Playing Roulette using the Martingale strategy')
    plt.gcf().canvas.set_window_title('Roulette Simulation')  # Window title
    plt.show()

    # Close the logger
    logging.shutdown()

if __name__ == '__main__':
    main()
