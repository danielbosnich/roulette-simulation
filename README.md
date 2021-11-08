# roulette-simulation
Roulette simulation using a one zero board and the Martingale betting strategy


# What is the Martingale strategy?
This is a common betting strategy for games with two outcomes like flipping a coin or, in this case, betting on red or black in roulette.  This strategy tells the gambler to double the amount bet after every loss until eventually winning, such that the amount won will always equal the original bet.  Of course, the problem with this strategy is that an exceptional string of consecutive losses can quickly bankrupt the gambler.


# Does this strategy work?
The Martingale strategy may sound enticing but, as with all roulette strategies, it will not make money in the long run.  If the table bet maximum is high enough, this strategy can even make a profit around 90% of the time.  The problem is that the wins (though many) will be small, while the losses will be substantial.


# Usage
Simply run the simulation file; there are no parameters

`python roulette_simulation.py`


# Simulation variables
The following variables can be updated to allow for different simulation results and to test for optimal strategy

`num_bets` The number of bets placed per sitting

`bank_start` The amount of money when starting

`starting_bet_size` The baseline bet size

`bet_size_limit` The maximum bet size allowed


# Example
Here's an example plot for a simulation with the following variables:
```
num_bets = 25
bank_start = 500
starting_bet_size = 2
bet_size_limit = 100  # Max bet size in Colorado
```

![Screenshot](https://github.com/danielbosnich/roulette-simulation/blob/main/example_plot.png)
