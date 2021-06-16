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
        3: Help
        4: Exit

        Please enter your choice: """)
        if not (choice == '1' or choice == '2' or choice == '3' or choice == '4'):
            print("Please enter valid menu selction")
            print()
        else:
            break


    if choice == '1':
        if os.path.exists("C:/Users/{}/Documents/BranchCompareOutput/AllBranches/BranchCompareAll.txt".format(getpass.getuser)):
            input("BranchCompareAll File already Exists. You will overide it. Press Enter to Continue")
        BranchCompareFunctions.setupBranchComparison()
        BranchCompareFunctions.runBranchComparison()
        main()

    elif choice == '2':
        if os.path.exists("C:/Users/{}/Documents/BranchCompareOutput/AllBranches/BranchCompareAll.txt".format(getpass.getuser)):
            filterResultsFunctions.filterSetup()
        else:
            print('''
            BranchCompareAll.txt does not exist.
            (will be found in C:/Users/Users/Documents/BranchCompareOutput/AllBranches)
            You must run Option 1 first.
            
            ''')
        menu()

    elif choice == '3':
        print('''
            Help Menu

                Option 1: 
                    Use this option to create a file containing all the differences 
                    between branches. The file will output to Documents/BranchCompareOutput/AllBranches
                    THIS MUST BE RAN BEFORE OPTION 2.
                Option 2:
                    Use this option to filter through the BranchCompareAll file (created
                    with option1). The path used should be what is found after CoreFW repository.
                    (i.e. "Tools/Firmware/EasyTester/Source")
                Option 4:
                    Use this option to exit the application.
        ''')
        input("Press Enter To Return To Menu")
        menu()

    else:
        print("Exited")
    