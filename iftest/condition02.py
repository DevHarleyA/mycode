#!/usr/bin/env python3

def main():
    # prompt the user for the host name
    hostname = input("What value should we set for hostname?")
    
    # set up the conditional for the script to respond with a print statement
    if hostname == "MTG":
        print("The hostname was found to be MTG")

main()

