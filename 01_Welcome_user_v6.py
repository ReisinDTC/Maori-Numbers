"""Component 1 - Welcome_user_v6
Simplifying the question for the instructions"""


# Functions go here...
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Gives instructions'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Program continues'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "Yes":
    print("Gives Instructions")
else:
    print("Program continues")
