# diceRoll.py - takes in a newline-separated set of dice rolls and returns values for each one

import re, random
challenge_input = "5d12\n6d4\n1d2\n1d8\n3d6\n4d20\n100d100"
for dice in re.findall(r'\d+d\d+', challenge_input):
    total = 0
    number_of_rolls = int(re.search(r'\d+', dice).group())
    die_value = int(re.search(r'd\d+', dice).group()[1:])
    for roll in range(number_of_rolls):
        total += random.randint(1,die_value)
    print(total)
