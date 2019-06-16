import random
# setting a varialble to first roll the dice
roll_again = "yes"

# setting limits for the values of dice
min = 1

max = 6

while roll_again == "yes" or roll_again == "y":

    print("Rolling the dices...")

    print("The values are....")

    print(random.randint(min, max))

    print(random.randint(min, max))

    roll_again = input("input yes or y to roll the dices again = ")

