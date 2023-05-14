"""Component 3 - Questions
The quiz will ask them at random """

import random

# This uses two ordinary lists

print("This is a test about the Maori numbers and you will need to\n"
      "get a question correct to earn a point.\n")

# 1st list
numbers = ["Tahi", "Rua", "Toru", "Whā", "Rima", "Ono", "Whitu", "Waru",
            "iwa", "tekau"]
# 2nd list
english_words = ["one", "two", "three", "four", "five", "six", "seven",
                    "eight", "nine", "ten"]

question = random.choice(numbers)
attempt = input(f"What is the english word for {question}: ")

# Using the position of the question to find the answer on the 2nd list
answer_index = numbers.index(question)
answer = english_words[answer_index]


# To connect the question to the answer
if attempt == answer:
    print("##### Correct #####")
else:
    print("!!!!! Incorrect !!!!!")
