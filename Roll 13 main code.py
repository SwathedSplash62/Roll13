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
    roll_result = random.randint(1, 6)
    return roll_result


def two_rolls(who):
    double_score = "no"

    roll_1 = dice_roll()
    roll_2 = dice_roll()

    if roll_1 == roll_2:
        double_score = "yes"

    # total amount of points so far
    first_points = roll_1 + roll_2

    # show the result
    print(f"Die 1: {roll_1}  Die 2: {roll_2}")

    return first_points, double_score


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
print("Press <enter> to begin this round: ")
input()

# Get initial dice rolls for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]

# Tells the user if they are able to get those double points
if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you gain double points!))))"

# output initial move results
print(f"You rolled a total of {user_points}. {double_feedback}")
print()

# Get the first dice rolls from the computer
computer_first = two_rolls()
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}.")

# Loop (while both user / computer have <= 13 points)....

while computer_points < 13 and user_points < 13:

    # ask user if the want to roll again, update points and status
    print()
    roll_again = input("Do you want to roll the dice (type 'no' to pass): ")
    if roll_again == "yes":
        user_move = dice_roll()
        user_points += user_move

        if user_points > 13:
            print(f"YOU FOOL, YOU WERE UNLUCKY, having rolled a {user_move} "
                  f"so you unfortunately have a total of {user_points}. The name of the game being 🎲🎲🎲Roll13🎲🎲🎲, "
                  f"you are over"
                  f"and have such lost")

            user_points = 0

            break

        else:
            print(f"You rolled one of them {user_move} and got a whole {user_points}")

    # roll dice for comp and update comp points
    computer_move = dice_roll()
    computer_points += computer_move
    if computer_points > 13:
        print(f"THAT FOOL, IT T'WAS UNLUCKY, having rolled a {computer_move} "
              f"so it fortunately has a total of {computer_points}. The name of the game being 🎲🎲🎲Roll13🎲🎲🎲, "
              f"it is over"
              f"and you have won")

        computer_points = 0

        break
    else:
        print(f"This damn machine just got {computer_move}. Adding for a whole {computer_points}.")

    print()
    if user_points > computer_points:
        result = "You are currently better than the robot"
    elif user_points < computer_points:
        result = "You are currently worse than the robot"
    else:
        result = "You both currently suck"

    statement_generator("Status update", "🐰🐰")
    print(f"{result}")
    print(f"User Score: {user_points} \t | \t Computer Score; {computer_points}")

# Outside loop - double user points if  they won and are eligible

# Le result
if user_points < computer_points:
    print("You have seen bested by thy metallic entity, "
          "thus no points have been added to your total score. Unfortunately meaning that your opposition has received"
          f" {computer_points} points.")

# Don't have them double points
else:
    print(f"You have better than that machine in the machine and gotten those {user_points} points")

print()
print("   Thank you for playing")
statement_generator("Roll13", "🎲")
print()
