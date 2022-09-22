#!/usr/bin/env python3
    
def main():
    
    file = input("What file would you like to load?")

    # add line counter
    lines = 0

    ## create file object in "r"ead mode
    with open(file, "r") as configfile:
        ## readlines() creates a list by reading target
        ## file line by line
        configlist = configfile.readlines()
        for line in configlist:
            lines += 1

        # pritn # of lines
        print(f"Number of lines: {lines}")
    ## file was just auto closed (no more indenting)

    ## each item of the list now has the "\n" characters back
    print(configlist)

main()
