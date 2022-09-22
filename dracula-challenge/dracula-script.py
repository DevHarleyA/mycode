#!/usr/bin/python3
"""Dracula Challenge - Loop through the Dracula.txt to determine how many times the word Dracula comes up."""

def main():
    
    # establish counter
    vampire_counter = 0

    # Read in the content of the Dracula novel as a file object
    with open("/home/student/mycode/dracula-challenge/dracula.txt") as spooky:
        with open("vampytimes.txt", "w") as vamp:
            # loop through the file
            for line in spooky:
                # if the word vampire is in the line, increase the counter
                if "vampire" in line.lower():
                    vampire_counter += 1
                    print(line)
                    vamp.write(line)
        
    # print out results
    print(f"Vampire occured {vampire_counter} times in the text.")
    
main()
