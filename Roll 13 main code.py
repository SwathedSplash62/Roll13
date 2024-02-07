def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions/information", "-")
    print()
    print("Please choose a number than is greater than or equal to one and less than or equal to 200")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each "
          "calculation or any key to quit.")
    print()
    return ""


# Main routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Displays instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()
