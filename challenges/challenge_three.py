#!/usr/bin/env python3

"""
Challenge: Attempt these challenges in increasing difficulty!

Part 1. Find your name in the classinfo dictionary below. Write code that prints your first name from the classinfo data shown here.

Part 2. Find your name in the classinfo dictionary below. Write a script that outputs ONE of the following using the classinfo dictionary below. (fill in the blank!):

My name is ______ and my spirit animal is _______.

My name is ______ and my skills are _______.

My name is ______ and my super power is _______.

Part 3. Write a script that loops through the entire classinfo dictionary. Have it output the following for every person in class.


A.Harley Response to Challenge
TLG || Alta3
"""

# Data to be sorted through

classinfo = {
    "all": [
        {
            "name": "Aaron",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Alexandra",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Alice",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Angela",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Ayrat",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Blake",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Shape of: A Giant Shark",
        },
        {
            "name": "Brandon",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Carl",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Transformation",
        },
        {
            "name": "Chris",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Pyrokinesis",
        },
        {
            "name": "Christian",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Deepak",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Explosive Shouts",
        },
        {
            "name": "Dennis",
            "skill level": "great",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Felicia",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Zoolingualism",
        },
        {
            "name": "Gabriel",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Height Manipulation",
        },
        {
            "name": "Julian",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Hydrokinesis",
        },
        {
            "name": "Kelly",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Lashay",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Stretchy",
        },
        {
            "name": "Nabin",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Steel Skin",
        },
        {
            "name": "Pratibha",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Teleportation",
        },
        {
            "name": "Quentin",
            "skill level": "remarkable",
            "spirit animal": "Lynx",
            "super power": "Polyglot",
        },
        {
            "name": "Will",
            "skill level": "super",
            "spirit animal": "Fox",
            "super power": "Eat Anything",
        },
    ]
}

def main():
    global classinfo


    name = classinfo["all"][1]["name"]

    # 1: Write code that prints your first name from the classinfo data shown 
    print("Print my name from the list: ")
    print("My name is: " + classinfo["all"][1]["name"])

    # 2: Write code that prints out one of the details information
    skill = classinfo["all"][1]["skill level"]
    sa = classinfo["all"][1]["spirit animal"]
    power = classinfo["all"][1]["super power"]

    print(f"My name is {name} and my spirit animal is {sa}.")
    print(f"My skills are {skill}.")
    print(f"My super power is {power}.")

    #3: Loop through all of the students and print a sentence about them.

    for student in classinfo["all"]:
        print(student["name"] + " a/an " + student["skill level"] + " " + student["spirit animal"] + " possesses a " + student["super power"] + " factor for moonlighting as a suprehero!")


main()
