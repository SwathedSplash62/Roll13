import random


def num_check(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is 13 or more"

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response > 12:
                print("You have chosen {} as your target score".format(response))
                return response

            # Outputs error if input is invalid
            else:
                print(error)

        except ValueError:
            print(error)
            print()


def yes_no(question):
    while True:
        response = input(question).lower()
        # checks user response to question
        # only accepts yes or no
        if response == "yes" or response == "y":
            instructions()
            return ""

        elif response == "no" or response == "n":
            print("You chose no")
            return ""

        else:
            print("Please answer yes or no ")


def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def dice_roll():
    result = random.randint(1, 6)
    return result


def two_rolls():
    double_score = "no"

    roll_1 = dice_roll()
    roll_2 = dice_roll()

    if roll_1 == roll_2:
        double_score = "yes"

    # total amount of points so far
    user_points = roll_1 + roll_2

    # show the result
    print(f"Die 1: {roll_1}  Die 2: {roll_2}  Points: {user_points}")
    print(f"Double score opportunity: {double_score}")

    return user_points, double_score


def instructions():
    statement_generator("Instructions/information", "-")
    print('''
At the start of each round, the user and the computer each roll two dice.
The initial number of points for each player is the total shown by the dice.Then, taking turns, 
the user and computer each roll a single die and add the result to their points.  
The goal is to get 13 points (or slightly less) for a given round.  
Once you are happy with your number of points, you can ‘pass’.

    -If you go over 13, then you lose the round (and get zero points). If the computer goes over 13, 
    the round ends and your score is the number of points that you have earned.
          
    -If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays 
    the same).
          
    -If you get more points than the computer (but less than 14 points), you win and add your points to your 
    score. The computer’s score stays the same.
          
    -The first roll of your dice is a double, then your score is increased by double the number of points, 
    provided you win.  If the computer’s first roll of the dice is a double, 
    then its points are not doubled (this gives the human player a slight advantage).
          
    -The ultimate winner of the game is the first one to get to the specified score goal.
    calculation or any key to quit.''')
    print()
    return ""


# Heading
statement_generator("Roll13", "🎲")

# Displays instructions if user has not used the program before
yes_no("Would you like to see the instructions? ").lower()

# Main routine goes here
keep_going = ""
while keep_going == "":
    target_score = num_check("Enter an integer that is 13 or more: ")
    # dice
    two_rolls()
    # double?

how_many = int(input("How many dice? "))

for item in range(0, 5):

    if how_many == 2:
        start_points = two_rolls()
        points = start_points[0]
        double_points = start_points[1]

    if double_points == "no":

        print(f"You have {points} points and a double ")

    user_first = two_rolls()
print()
print("   Thank you for playing")
statement_generator("Roll13", "🎲")
print()
