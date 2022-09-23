#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# import the crayons package to apply color to the document
import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(crayons.green(f'Handshaking. .. ... connecting with {ip}')) # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(crayons.cyan(f'Attempting to sending command --> {mycmds}'))
            # we'll learn to write code that sends cmds to device here
    return None

# function to reboot device
def devicereboot(ip_list): # ip_list = list of IPs
    # loop through the ip addresses in the list
    for ip in ip_list:
        # print out each ip address
        print(crayons.yellow(f"Connecting to: {ip}"))
        # print rebooting now after the ip address
        print(crayons.yellow("REBOOTING NOW!"))
    return None

# start our main script
def main():
    """called at runtime"""

    with open("devicemd.json", "r") as devicemdfile:
        devicemd = json.load(devicemdfile) # decode the JSON from the file to pythonic data
    
    # list of only IPs
    ip_list = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    # run reboot
    devicereboot(ip_list) # call function to reboot all devices

# call our main function
main()

