"""Component 3 - Questions_v3
they can choose what they want to answer the questions like"""

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
choice = input("Enter test: 'L' to answer lower case words, 'U' to answer upper case words, 'N' to answer in numbers"
               " and not words:  ")
if choice == "L":
    choice = lower_case
if choice == "U":
    choice = upper_case
if choice == "N":
    choice = numbers


random.shuffle(choice)

for i in choice:
    answer = input("Enter the english word in lower case for {}: ".format(i[0]))
    if answer == i[1]:
        print("CORRECT")

    else:
        print("INCORRECT")
