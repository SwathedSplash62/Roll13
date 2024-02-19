import random


def get_stats(stats_list):
    stats_list.sort()

    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]


# calculate the lowest highest and average scores and display them

def num_check(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is 13 or more"

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= 13:
                print("You have chosen {} as your target score".format(response))
                return response

            # Outputs error if input is invalid
            else:
                print(error)

        except ValueError:
            print(error)
            print()


def yes_no_instructions(question):
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


def yes_no(question):
    while True:
        response = input(question).lower()
        # checks user response to question
        # only accepts yes or no
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

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
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

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


# initial scores for both parties / also number of rounds
user_score = 0
computer_score = 0

num_rounds = 0

user_scores = []
comp_scores = []
game_history = []

# Main routine goes here

# Heading
statement_generator("Roll13", "🎲")

# Displays instructions if user has not used the program before
yes_no_instructions("Would you like to see the instructions? ").lower()
target_score = num_check("Enter a target score: ")
print(target_score)

# round numberer

while user_score < target_score and computer_score < target_score:

    # Start of a single round

    # computer / user free will
    user_pass = "no"
    computer_pass = "no"

    # the start button / Start of a single round
    print("Press <enter> to begin this round: ")
    input()

    num_rounds += 1
    print(f"🔗🔗🔗 Round {num_rounds} 🔗🔗🔗")

    # Get initial dice rolls for user
    user_first = two_rolls("User")
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
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    print(f"The computer rolled a total of {computer_points}.")

    # Loop (while both user / computer have <= 13 points)....

    while computer_points <= 13 and user_points <= 13:

        # ask user if the want to roll again, update points and status
        print()

        if user_points == 13:
            user_pass = "yes"

        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type 'no' to pass): ")

        else:
            roll_again = "no"

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

        else:
            # they no
            user_pass = "yes"

        # comp free will
        if computer_points >= 10 and computer_points >= user_points and user_pass >= "no":
            computer_pass = "yes"
            print("The computer, assured in it's advantage has passed")

        elif computer_pass == "yes":
            pass

        else:
            # roll dice for comp and update comp points
            computer_move = dice_roll()
            computer_points += computer_move

            if computer_points > 13:
                print(f"THAT FOOL, IT T'WAS UNLUCKY, having rolled a {computer_move} "
                      f"so it fortunately has a total of {computer_points}. The name of the game being 🎲🎲🎲Roll13🎲🎲🎲, "
                      f"it is over"
                      f" and you have 🎉🎉🎉🎉🎉🎉🎉🎉won🎉🎉🎉🎉🎉🎉🎉")

                computer_points = 0

                break
            else:
                print(f"This damn machine just got {computer_move}. Adding for a whole {computer_points}.")

        print()
        if user_points > computer_points:
            result = "👍👍👍👍🤖You are currently better than the robot🤖👍👍👍👍"
        elif user_points < computer_points:
            result = "👎👎👎👎🤖You are currently worse than the robot🤖👎👎👎👎"
        else:
            result = "👎👎👎👎You both currently suck👎👎👎👎"

        statement_generator("Status update", "🐰🐰")
        print(f"{result}")
        print(f"User Score: {user_points} \t | \t Computer Score; {computer_points}")

        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside loop - double user points if  they won and are eligible

    # Le result
    if user_points < computer_points:
        print("You have seen bested by thy metallic entity, "
              "thus no points have been added to your total score. Unfortunately meaning that your opposition has "
              "received"
              f" {computer_points} points.")

        add_points = computer_points

    elif user_points > computer_points:
        # Double pts checker
        if double_points == "yes":
            user_points *= 2
        print(f"You are better than that machine in the machine and gotten those {user_points} points")

        add_points = user_points

    else:
        print(f"You are both boring and have the same amount of {user_points}, meaning you both get {user_points}"
              f" added to your total")

        add_points = user_points

    round_result = f"Round {num_rounds} - User {user_points} \t Computer: {computer_points}"
    game_history.append(round_result)
    # End of a single round

    # If the computer wins, add its points to its score
    if user_points < computer_points:
        computer_score += add_points

    # if the user wins, add their points to their score
    elif user_points > computer_points:
        user_score += add_points

    # if it's a tie, add the points to both scores
    else:
        computer_score += add_points
        user_score += add_points

        user_scores.append(user_score)
        comp_scores.append(computer_score)

    print()
    print(f"🎲🎲🎲 User: {user_score} points | Computer: {computer_score} points 🎲🎲🎲 ")
    print()

print()
print(f"Your final score is {user_score}")

# game lore
show_history = yes_no("Do you want to see the game history")
if show_history == "yes":
    print("\n🎃🎃🎃 Game History 🎃🎃🎃")

    for item in game_history:
        print(item)

    print()


# Behol, stats
user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)

print("📈📈📈 Game Statistics 📈📈📈")
print(f"User -     Lowest Score:, {user_stats[0]}\t Highest Score; {user_stats[1]}\t Average Scores: {user_stats[2]:.2f}")

print(f"Computer - Lowest Score:{comp_stats[0]}\t Highest Score: {comp_stats[1]}\t Average Scores: {user_stats[2]:.2f}")

print("   Thank you for playing")
statement_generator("Roll13", "🎲")
print()
