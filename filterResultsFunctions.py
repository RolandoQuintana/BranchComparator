import getpass


def filterSetup():

    userName = getpass.getuser()

    allBranchFile = open("C:/Users/{}/Documents/BranchCompareOutput/AllBranches/BranchCompareAll.txt".format(userName), 'r')

    allBranchContent = allBranchFile.read()


    while True:
        print("")
        filterFileName = input("Please input desired name of this filter results: ")

        if filterFileName == "BranchCompareAll":
            print("File name cannot be the same as BranchCompareAll")
        
        else:
            print("")
            break

    filterFile = open("C:/Users/{}/Documents/BranchCompareOutput/Filtered/{}.txt".format(userName, filterFileName), 'w')

    filterPath = input("Please enter the path you would like to filter: ")



    for line in allBranchContent.split('\n'):

        if '-' in line:
            if filterPath in line:
                filterFile.write(line+'\n')
        elif '+' in line:
            if filterPath in line:
                filterFile.write(line+'\n')
        else:
            filterFile.write(line+'\n')

    print("")
    print("FINISHED")
    print("{} saved in C:/Users/{}/Documents/BranchCompareOutput/Filtered/{}.txt".format(filterFileName, userName, filterFileName))
    print("")
    print("Press Enter to return to Main Menu")

