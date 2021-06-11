import os
import filecmpModified
import subprocess
import getpass
import BranchCompareFunctions
import filterResultsFunctions


def main():
    print("")
    print("")
    print("___Welcome To Branch Compare___")
    print("")
    menu()


def menu():
    
    while True:

        choice = input("""
        1: Run Branch Comparison For CoreFW
        2: Filter Branch Comparison Results
        3: Exit

        Please enter your choice: """)
        if not (choice == '1' or choice == '2' or choice == '3'):
            print("Please enter valid menu selction")
            print()
        else:
            break


    if choice == '1':
        BranchCompareFunctions.setupBranchComparison()
        BranchCompareFunctions.runBranchComparison()
        main()

    elif choice == '2':
        filterResultsFunctions.filterSetup()
        menu()

    else:
        print("Exited")
    