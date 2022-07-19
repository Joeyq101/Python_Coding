# Program that simulates rolling a single dice
# Import the random module
import random

# set while loop variable roll_again to determine if the player wants to roll again
roll_again = 1
# while loop to continue playing after rolling
while roll_again == 1:
    roll_amount = int(input("How many times would you like to roll the dice?\n"))
    # iterating through a for loop roll_amount of times
    for i in range(1,roll_amount + 1):
        roll_value = random.randint(1,6)
        print(f"roll {i} is: {roll_value}")

    # asking player to change value of roll_again if they would like to exit
    roll_again = input("Would you like to roll again? 'yes' or 'no'\n")
    # if player says no, roll_again = 0 and while loop will not execute again, program will exit
    if roll_again == 'no':
        roll_again = 0
    # if player says yes, roll_again = 1 and while loop will execute again
    elif roll_again =='yes':
        roll_again = 1
