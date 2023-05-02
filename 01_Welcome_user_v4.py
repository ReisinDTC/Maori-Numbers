"""Component 1 - Welcome_user_v3
It will accept lower case letters
"""


show_instructions = ""
while show_instructions != "x":

    #Ask the user if they have played before
    show_instructions = input("Would you like the instructions of this quiz?: ")

    #If they say yes, output 'Program Continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    #If they say no, output 'Display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    #Otherwise - show error
    else:
        print("Please answer 'yes' or 'no'")

    print(f"You entered '{show_instructions}'")
