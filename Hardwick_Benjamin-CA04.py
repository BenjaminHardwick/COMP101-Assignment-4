# Hardwick_Benjamin-CA04.py
# November 2018
# Create a marking system that will deduct 5 marks every day it is overdue.
# This aims to test our programming abilities and to help engage using
# for loops, and while loops.
import sys
# Function sits at the top because it cannot call a function lower than it.
def marking_again():
    marking_loop = input("Select what you want to do next. \n A. Menu \n B. Marking \n X. Exit \n Type your letter of selection here:   ")
    marking_loop = marking_loop.upper()
    if marking_loop == 'X':
        exit()
        print("Taking to you to the marking module!")
    elif marking_loop == 'B':
        marking()
    elif marking_loop == 'A':
        menu()
# Defining each module that sits within the program, this allows the defined module to be called.
def marking():
# Validating the program to only allow integers that are either smaller that 100, or greater than 0.
    print("--------------------- MARKING MODULE--------------------- ")
    print("Welcome to the University Marking Module")
    print()
    while True:
        overall_mark = int(input("Enter the mark of the coursework (Between 0  and 100):  "))

        if overall_mark < 0:
            print("Invalid entry, entries must be greater than 0.")
            continue
        elif overall_mark > 100:
            print("Invalid entry, entries must be less than 100.")
            continue
        else:
            break

# Also validating the program here to only allow the input to be integers smaller than 12, or greater than 0.
    while True:
        overdue = int(input("Enter the amount of days overdue this assignment is: "))
        if overdue < 0 :
            print("Invalid entry. Entries must be greater than 0.")
            continue
        elif overdue > 12:
            print("Invalid entry. Entries must be smaller than 12 days.")
            continue
        else:
            break

# Creating a loop for the calculations.

      # What's going on here is creating the variables before entering them into the loop.
    daysCounted = 0
    if overall_mark < 40:
        print("Fail at,",overall_mark)
    elif overall_mark == 40:
        print("this is the minimum pass rate you pass at 40")

    while overall_mark > 40 and daysCounted != overdue:
        overall_mark = (overall_mark - 5)
        daysCounted = daysCounted + 1               # Here we have created the variables so they constantly loop until it reaches
                        # 40, it will not display integers smaller than 40. And finally it will cap the mark at 40.
        if overall_mark<=40:
            overall_mark=40
        print("Days Overdue:", daysCounted, "Final Mark:", overall_mark)

    print()
    print()
    marking_again()

# Opening a definition for the loop to then ask the user if they would like to mark again, exit or go to the menu.





def extend():
    print("Undergoing development.")
    menu()


def exit():
    sys.exit()

# Menu, using a while loop, also validated so the user cannot input anything other than A, E, or X.
def menu():
    userInput = ""
    while userInput != "X":
        print("\n\n\n--------------Main Menu----------------\n\n\n")
        print("For the Marking, type 'A'.")
        print("For the Extend, type 'E'.")
        print("To exit the program, type 'X'.")
        userInput = input("\n\nEnter an option A, E or X: ")
        userInput = userInput.upper()

        while userInput not in ("A", "E", "X"):
            print("That is invalid")
            userInput = input("please select A, E or X: ")
            userInput = userInput.upper()

        if userInput == "A":
            marking()
        elif userInput == "E":
            extend()
        return

menu()
