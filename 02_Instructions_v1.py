"""Component 2 - Instructions_v1
Giving them instructions, so they can read and know what to do"""


# Functions go here...
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Give instructions'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Program Continues'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# function to display instructions
def instructions():
    print()
    print("**** How to complete quiz ****")
    print()
    print("There are 10 questions")
    print()
    print("Give the answer in English words")
    print()
    print("You have unlimited tries but you want a attempt score")
    print()
    print("Would you like to continue to play the quiz")


# Main routine go here...
played_before = yes_no("Do you want to have instructions? ")

if played_before == "Yes":
    instructions()
else:
    print("Program continues")
