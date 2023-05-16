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
    print("Give the answer in English words in lower case "
          "like two instead of Two, or four instead of Four ect.\n")
    print()
    print("You have unlimited tries but you want a attempt score")
    print()


# Making it continue if yes
def continues():
    print()
    print("Well then, Good luck and wish you the very best of luck!")

# Ending the quiz if they say No
def giving_up():
    print()
    print("Maybe next time. ")


# Main routine go here...
played_before = yes_no("Do you want to have instructions? ")

if played_before == "Yes":
    instructions()
else:
    print("Program continues")

continues_playing = input("Do you want to continue with the quiz? ")

if continues_playing == "yes":
    continues()
elif continues_playing == "Yes":
    continues()
elif continues_playing == "y":
    continues()
elif continues_playing == "no":
    giving_up()
elif continues_playing == "No":
    giving_up()
elif continues_playing == "n":
    giving_up()
else:
    print("Plz answer yes or no")
