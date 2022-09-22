#!/usr/bin/env python3

"""Trying out colors in Python with the crayons import!"""

# import statement for installed crayons package
import crayons

def main():
    
    # print roses are red in red
    print(crayons.red("Roses are red..."))

    # print violets are blue in blue
    print(crayons.blue("Violets are blue..."))

    # print elmo watches you in your sleep in magenta
    print(crayons.magenta("Elmo watches you in your sleep", bold=True))

    # print and Freddy does too! in green
    print(crayons.green("...and Freddy does too!", bold=True))

    # print Happy Halloween without color
    print("Happy Halloween!")

if __name__ == "__main__":
    main()
