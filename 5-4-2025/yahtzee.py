# yahtzee_yourname.py

import numpy as np
import random

# -------------------------------------------------
# Computer Science, Project 14
# November 14, 2017
# Partner 1 Name, Partner 2 Name
# -------------------------------------------------
# Describe the contributions you and your partner
# made to your solution.
# -------------------------------------------------






np.all




def roll_dice(roll):
    """Simulate rolling five six-sided dice by assigning random values from 1–6."""
    for i in range(len(roll)):
        roll[i] = random.randint(1, 6)  # Random int between 1 and 6
    return roll


def count_outcomes(results):
    """
    Count how many times each number (1 through 6) appears in the roll.
    Returns a list of size 7 (index 0 unused) with counts for each die face.
    Example: if results = [2, 3, 2, 2, 5] then counts = [0, 0, 3, 1, 0, 1, 0]
    """
    counts = np.zeros(7, dtype=np.int16)  # index 0 unused; indices 1-6 used
    for die in results:
        counts[die] += 1
    return counts


def is_it_yahtzee(results):
    """
    Check if all five dice show the same number.
    Example: [4, 4, 4, 4, 4] → True
    """
    return np.all(results == results[0])  # All elements must equal the first die


def is_it_full_house(results):
    """
    Check for a full house: 3 of one number and 2 of another.
    Example: [2, 2, 5, 2, 5] → True
    """
    counts = count_outcomes(results)  # Get counts of each number
    return 3 in counts and 2 in counts  # Must contain one '3 of a kind' and one 'pair'


def is_it_large_straight(results):
    """
    Check for a large straight: either 1-2-3-4-5 or 2-3-4-5-6, in any order.
    Example: [3, 5, 4, 1, 2] → True
    """
    sorted_roll = sorted(results)  # Order matters here
    return sorted_roll == [1, 2, 3, 4, 5] or sorted_roll == [2, 3, 4, 5, 6]


# -------------------------------------------------
# Simulation Section
# This runs 5000 rolls and counts how many special hands appear.
# -------------------------------------------------

how_many = 5000  # Total number of simulated dice rolls
yahtzees = 0
full_houses = 0
large_straights = 0

roll = np.zeros(5, dtype=np.int16)  # Allocate space for 5 dice using NumPy array

# Run the simulation how_many times
for i in range(how_many):
    results = roll_dice(roll)  # Simulate rolling the dice

    # Check for Yahtzee first (most specific), then Full House, then Large Straight
    if is_it_yahtzee(results):
        yahtzees += 1
    elif is_it_full_house(results):
        full_houses += 1
    elif is_it_large_straight(results):
        large_straights += 1

# Print the results with percentages
print("Number of Rolls:", how_many)
print("---------------------")
print("Number of Yahtzees:", yahtzees)
print("Yahtzee Percent:", "{:.2f}%\n".format(yahtzees * 100 / how_many))
print("Number of Full Houses:", full_houses)
print("Full House Percent:", "{:.2f}%\n".format(full_houses * 100 / how_many))
print("Number of Large Straights:", large_straights)
print("Large Straight Percent:", "{:.2f}%".format(large_straights * 100 / how_many))
