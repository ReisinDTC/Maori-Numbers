"""Final_MN - Final version
fixed it up to make sure it works
"""


import random


def goodbye():
    print("Goodbye! Hope you enjoyed the quiz.")


def play(choice_):
    random.shuffle(choice_)
    score = 0

    for i in choice_:
        answer = input("Enter the English word in lower case for {}: ".format(i[0]))
        if answer.lower() == i[1]:
            print("CORRECT!")
            score += 1
        else:
            print("INCORRECT")

    print("Your score is:", score)


def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        if answer in ["yes", "y"]:
            return "Yes"
        elif answer in ["no", "n"]:
            return "No"
        else:
            print("Please answer 'yes' or 'no'")


def instructions():
    print("\n**** How to complete the quiz ****\n")
    print("There are 10 questions.")
    print("Give the answer in English words in lower case.")
    print("You have unlimited tries, but your score will be based on correct answers.\n")


def continues():
    print("\nGood luck and have fun!")
    choice_ = input("Enter 'L' to answer lower case words, 'U' to answer upper case words, "
                    "or 'N' to answer in numbers: ")

    if choice_ == "L":
        play(lower_case)
    elif choice_ == "N":
        play(numbers)
    else:
        print("Invalid choice. Please try again.")


def giving_up():
    print("\nMaybe next time. Quiz ends.")


# Main routine
lower_case = [["Tahi", "one"], ["Rua", "two"], ["Toru", "three"], ["Whā", "four"], ["Rima", "five"],
              ["Ono", "six"], ["Whitu", "seven"], ["Waru", "eight"], ["iwa", "nine"], ["Tekau", "ten"]]

numbers = [["Tahi", "1"], ["Rua", "2"], ["Toru", "3"], ["Whā", "4"], ["Rima", "5"],
           ["Ono", "6"], ["Whitu", "7"], ["Waru", "8"], ["iwa", "9"], ["Tekau", "10"]]

played_before = yes_no("Do you want to see the instructions? ")
if played_before == "Yes":
    instructions()

continues_playing = yes_no("Do you want to continue with the quiz? ")
if continues_playing == "Yes":
    continues()
else:
    giving_up()

enjoyed = yes_no("Did you enjoy this quiz? ")
if enjoyed == "Yes":
    print("Thank you!")
else:
    print("Sorry about that.")

goodbye()
