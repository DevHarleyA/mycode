#!/usr/bin/env python3

"""Exercise: lists, input, print, concatenate, variables"""

import random

def main():
    # put list in code
    wordbank= ["indentation", "spaces"] 
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # append the integer 4 to wordbank
    wordbank.append(4)
    
    # input asking for number between 0 and 18
    print("Enter a number between 0 and 18, enter a students name, or type 'random'")

    # assign the user's response to a variable
    choice = input("type your decision: ")

    # if user input is a number, assign to student_name
    if choice.isdigit():
        student_name = tlgstudents[int(choice)]

    # else if the user response is a name from the list, assign to student_name
    elif choice in tlgstudents:
        student_name = choice

    # else the choice is random
    else:
        student_name = random.choice(tlgstudents)

    # print strings using list components and variables (text provided)
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


main()
