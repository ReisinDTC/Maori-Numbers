"""Component 3 - Questions_v2
The quiz will hopefully repeat it's self we can have 10 questions"""

import random

# This uses two ordinary lists

print("This is a test about the Maori numbers and you will need to\n"
      "get a question correct to earn a point. Plz put a lower case as two, four instead of Four ect, as this will "
      "be incorrect.\n")

# 1st list
numbers = [["Tahi", "one"], ["Rua", "two"], ["Toru", "three"], ["Wha", "four"], ["Rima", "five"],
           ["Ono", "six"], ["Whitu", "seven"], ["Waru", "eight"], ["iwa", "nine"], ["tekau", "ten"]]

choice = input("Enter test: 'N' to start the quiz:  ")
if choice == "N":
    choice = numbers


random.shuffle(choice)

for i in choice:
    answer = input("Enter the english word in lower case for {}: ".format(i[0]))
    if answer == i[1]:
        print("CORRECT")

    else:
        print("INCORRECT")
