"""Component 3 - Questions_v3
they can choose what they want to answer the questions like plus put in a score to see how many they got right
"""

import random

# This uses two ordinary lists

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

print("\nGood luck and have fun!")
choice_ = input("Enter 'L' to answer lower case words, 'U' to answer upper case words, "
                "or 'N' to answer in numbers: ")


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


if choice_ == "L":
    play(lower_case)
elif choice_ == "U":
    play(upper_case)
elif choice_ == "N":
    play(numbers)
else:
    print("Invalid choice. Please try again.")




