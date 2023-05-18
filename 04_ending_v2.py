""" Component 4 - ending_v2
"""

import random


def goodbye():
    print("Goodbye, hope you enjoyed that and maybe play again!"
          " Enjoy the rest of the marking Mr Baker. ")


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
