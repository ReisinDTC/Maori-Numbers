"""00_MNN_Base_v1
This is the code without the last component"""


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
    play()


# Ending the quiz if they say No
def giving_up():
    print()
    print("Maybe next time. ")
    print("Quiz ends")


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

show_instructions = ""
while show_instructions != "x":

    # Ask the user if they have played before
    show_instructions = input("Would you like the instructions of this quiz?: ")

    # If they say yes, output 'Program Continues'
    if show_instructions == "yes" or show_instructions == "Yes" or show_instructions == "y":
        print("Program continues")
        instructions()

    # If they say no, output 'Display instructions'
    elif show_instructions == "no" or show_instructions == "No" or show_instructions == "n":
        print("Program continues")

    # Otherwise - show error
    else:
        print("Please answer 'yes' or 'no'")

    print(f"You entered '{show_instructions}'")


import random

# This uses three ordinary lists

print("This is a test about the Maori numbers and you will need to\n"
      "get a question correct to earn a point. Plz put a lower case as two, four instead of Four ect, as this will "
      "be incorrect.\n")

# 1st list
lower_case = [["Tahi", "one"], ["Rua", "two"], ["Toru", "three"], ["Whā", "four"], ["Rima", "five"],
                ["Ono", "six"], ["Whitu", "seven"], ["Waru", "eight"], ["iwa", "nine"], ["Tekau", "ten"]]
# 2nd list
upper_case = [["Tahi", "One"], ["Rua", "Two"], ["Toru", "Three"], ["Whā", "Four"], ["Rima", "Five"],
                 ["Ono", "Six"], ["Whitu", "Seven"], ["Waru", "Eight"], ["iwa", "Nine"], ["Tekau", "Ten"]]
# 3rd list
numbers = [["Tahi", "1"], ["Rua", "2"], ["Toru", "3"], ["Whā", "4"], ["Rima", "5"],
           ["Ono", "6"], ["Whitu", "7"], ["Waru", "8"], ["iwa", "9"], ["Tekau", "10"]]


def play():
    choice_ = input("Enter test: 'L' to answer lower case words, 'U' to answer upper case words, "
                   "'N' to answer in numbers and not words: ")
    if choice_ == "L":
        choice_ = lower_case
    if choice_ == "U":
        choice_ = upper_case
    if choice_ == "N":
        choice_ = numbers


    random.shuffle(choice_)

    for i in choice_:
        answer = input("Enter the english word in lower case for {}: ".format(i[0]))
        if answer == i[1]:
            print("CORRECT")

    else:
        print("INCORRECT")
