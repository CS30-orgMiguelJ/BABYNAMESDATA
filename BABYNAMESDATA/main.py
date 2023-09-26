# BABY NAMES DATA ASSIGNMENT START CODE

import json


def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    file.close()

    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL")
    for i in range(len(baby_data)):
        print(f"{baby_data[i]['name']} (Rank: {baby_data[i]['rank']}, Gender: {baby_data[i]['gender']})")


def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    print("\nSEARCH BY GENDER")
    gender = input("Enter a gender (Boy/Girl)(case sensitive): ")
    for i in range(len(baby_data)):
        if baby_data[i]['gender'] == gender:
            print(f"{baby_data[i]['name']} (Rank: {baby_data[i]['rank']}, Gender: {baby_data[i]['gender']})")


def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")
    min_rank = int(input("Enter a minimum rank: "))
    max_rank = int(input("Enter a maximum rank: "))
    _ = 0
    for i in range(len(baby_data)):
        if int(baby_data[i]['rank']) >= min_rank and int(baby_data[i]['rank']) <= max_rank:
            _ +=1
            print(f"{baby_data[i]['name']} (Rank: {baby_data[i]['rank']}, Gender: {baby_data[i]['gender']})")
    print(f"Number of names found: {_}")


def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER")
    starting_letter = input("Enter a starting letter: ").upper()
    _ = 0
    for i in range(len(baby_data)):
        if baby_data[i]['name'][0] == starting_letter:
            _ += 1
            print(f"{baby_data[i]['name']} (Rank: {baby_data[i]['rank']}, Gender: {baby_data[i]['gender']})")
    print(f"Number of names found: {_}")



def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
    name_length = int(input("Enter a name length: "))    
    _ = 0
    for i in range(len(baby_data)):
        if len(baby_data[i]['name']) == name_length:
            _ += 1    
            print(f"{baby_data[i]['name']} (Rank: {baby_data[i]['rank']}, Gender: {baby_data[i]['gender']})")
    print(f"Number of names found: {_}")




# Invoke main to begin program
main()
