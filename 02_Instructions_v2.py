"""Component 2 - Instructions_v2
Taking them to where the quiz begins if they would like to continue"""


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
            print("Program continues")

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


#
def continues():
    print()
    print("Well then, Good luck and wish you the very best of luck!")


# Main routine go here...
played_before = yes_no("Do you want to have instructions? ")

if played_before == "Yes":
    instructions()
else:
    print("Program continues")

continues_playing = input("Do you want to continue with the quiz? ")
giving_up = input("Maybe next time. ")

if continues_playing == "y" or "yes" or "Yes":
    continues()
if giving_up == "n" or "no" or "No":
    print("Maybe next time. ")
else:
    print("Plz answer Yes or No")
