"""Component 1 - Welcome_user_v5
Making sure that it will only work for Yes and No.
Anything else would have to make it answer the question again
"""


show_instructions = ""
while show_instructions != "x":

    # Ask the user if they have played before
    show_instructions = input("Would you like the instructions of this quiz?: ")

    # If they say yes, output 'Program Continues'
    if show_instructions == "yes" or show_instructions == "Yes" or show_instructions == "y":
        print("Program continues")

    # If they say no, output 'Display instructions'
    elif show_instructions == "no" or show_instructions == "No" or show_instructions == "n":
        print("Program continues")

    # Otherwise - show error
    else:
        print("Please answer 'yes' or 'no'")

    print(f"You entered '{show_instructions}'")
