# Program that simulates rolling a single dice
# Import the random module
import random

# Average function----------------------------------------------
def roll_average(rolls):
    # find the total amount of rolls by finding length of rolls list
    rolls_recieved = len(rolls)
    i = 0
    roll_total = 0
    # add up each roll in list roll and store in roll_total
    while i < rolls_recieved:
        roll_total += rolls[i] 
        i += 1
    # calculate the average roll
    roll_avg = roll_total/rolls_recieved
    # return average roll and roll total
    return int(roll_avg), roll_total
#----------------------------------------------------------------
# A function to list what the rolls were and print to console
def print_list(rolls):
    # find the total amount of rolls by finding length of rolls list
    rolls_recieved = len(rolls)
    # print each index of rolls list
    print("The roll list:")
    for i in range(1, rolls_recieved + 1):
        print(f"Roll {i} is {rolls[i-1]}")
        i += 1
#------------------------------------------------------------------

# set while loop variable roll_again to determine if the player wants to roll again
roll_list = []
# while loop to continue playing after rolling
while True:
    roll_amount = int(input("How many times would you like to roll the dice?\n"))
    # iterating through a for loop roll_amount of times

    for i in range(1, roll_amount + 1):
        roll_value = random.randint(1,6)
        # Storing dice rolls
        roll_list.append(roll_value)

    print(f"The role average is {roll_average(roll_list)[0]} and the roll total is {roll_average(roll_list)[1]} ")
    print_list(roll_list)

    # Append roll list as a string to readme.txt
    with open('readme.txt', 'a') as myfile:
        myfile.write(str(roll_list))
    # Store the data in a new list to output all of the entries so far
    with open('readme.txt') as myfile:
        new_roll_list = myfile.readline()

    print(f"txt file roll list: {new_roll_list}")

    # asking player to roll_again 
    roll_again = input("Would you like to roll again? 'y' or 'n'\n").lower()
    if roll_again == 'n':
        print("Thank you for playing")# breaks out of while loop
        break
    else:
        continue
#----------------------------------------------------------------------------------------







