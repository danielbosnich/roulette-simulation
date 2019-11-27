"""
Simulation of the Roulette Martingale Strategy

Created on Wed Jun 12 15:58:02 2019

@author: danielb
"""

# Package imports
import logging
import random
import time
import matplotlib.pyplot as plt

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
    num_plays = 5000
    num_bets = 20 # Number of bets per simulation
    bank_start = 5000
    starting_bet_size = 15
    bet_size_limit = 1250
    color_bet = RED
    wins = 0
    ending_bank_amounts = []

    # Seed the random number generator
    random.seed()

    # Start time
    start_time = time.time()

    # Start up logging
    logging.basicConfig(format='[%(asctime)s] %(levelname)s : %(message)s',
                        level=logging.INFO)

    for i in range(num_plays):
        # Reset the bank and the bet size
        current_bank = bank_start
        bet_size = starting_bet_size

        for j in range(num_bets):
            logging.debug("Placing bet # %i in simulation # %i", j, i)
            # Subtract money for the bet
            current_bank = current_bank - bet_size

            # Simulate a single run of the game
            winning_pocket = random.randint(0, 36)
            winning_color = POCKETS[winning_pocket]
            logging.debug('The winning pocket is  %s', winning_pocket)
            logging.debug('The winning color is %s', winning_color)

            # Check if the bet won
            if winning_color == color_bet:
                current_bank = current_bank + bet_size * 2
                bet_size = starting_bet_size
                logging.debug("Won. The bank amount is now: %i", current_bank)
            else:
                bet_size = bet_size * 2
                if bet_size > bet_size_limit:
                    bet_size = starting_bet_size
                logging.debug("Lost. The bank amount is now: %i", current_bank)

        # Check if we made money or lost money and add bank amount to list
        if current_bank > bank_start:
            wins += 1
        ending_bank_amounts.append(current_bank)


    # Figure out how many times we made money
    winning_percentage = wins / num_plays * 100
    logging.info("We made money %.3f percent of the times we played",
                 winning_percentage)

    # Create the histogram
    plt.hist(ending_bank_amounts, 80)
    plt.xlabel('Ending bank amount ($)')
    plt.ylabel('Frequency')
    plt.title('Playing Roulette using the Martingale strategy')
    plt.show()

    # Calculate program execution time
    end_time = time.time()
    execution_time = end_time - start_time
    logging.debug("It took the program %.3f seconds to run", execution_time)

    # Close the logger
    logging.shutdown()

if __name__ == '__main__':
    main()
