#!/usr/bin/python3

"""Printing dictionary data stored as lists to the screen"""

def main():

    # the data that we want to loop through. It is a list with three dictionaries
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


    for farm in farms:
        # print each farm name
        print(farm.get("name", "Unknown Farm"), end=":\n")

        # grab the agriculture for each farm with a nested loop
        for agri in farm.get("agriculture"):
            print("  -", agri)

if __name__ == "__main__":
    main()
