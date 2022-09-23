#!/usr/bin/env python3

# imports
import netifaces

# function to print only the IP address
def ipaddress(adapter_name):
    print("IP ONLY: ", end='')
    print(netifaces.ifaddresses(adapter_name)[netifaces.AF_INET][0]['addr'])


# function to print only the MAC address
def mac(adapter_name):
    print("MAC ONLY ", end='')
    print(netifaces.ifaddresses(adapter_name)[netifaces.AF_LINK][0]['addr'])

def main():
    
    # prints a list of our interfaces
    print(netifaces.interfaces())
    
    # create a loop to loop through the interfaces
    for i in netifaces.interfaces():

        # print a line that presents the interface
        print('\n**************Details of Interface - ' + i + ' *********************')
        
        try:
            # print a label
            print("MAC: ", end='')

            # print details about the interface we're looking at
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        

            # print label
            print("IP: ", end='')

            # tweaked to read AF_INET
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        
        except:

            # error message
            print("Could not collect adapter information.")
    
    for i in netifaces.interfaces():

        ipaddress(i)
    
    for i in netifaces.interfaces():
        mac(i)

main()
