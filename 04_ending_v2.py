""" Component 4 - ending_v2
saying goodbye and ending the code
"""

import random


def goodbye():
    print("Goodbye! Hope you enjoyed the quiz.")


enjoyed = input("Did you enjoy this quiz: ")

if enjoyed == "Yes":
    print("Thank you")
    goodbye()
elif enjoyed == "yes":
    print("Thank you")
    goodbye()
elif enjoyed == "y":
    print("Thank you")
    goodbye()
else:
    print("Sorry about that")
    goodbye()
