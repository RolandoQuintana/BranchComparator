import getpass
import os


def filterSetup():

    userName = getpass.getuser()

    allBranchFile = open("C:/Users/{}/Documents/BranchCompareOutput/AllBranches/BranchCompareAll.txt".format(userName), 'r')

    allBranchContent = allBranchFile.read()


    while True:
        print("")
        filterFileName = input("Please input desired name of the filter results: ")

        if filterFileName == "BranchCompareAll":
            print("File name cannot be the same as BranchCompareAll")
        
        else:
            print("")
            break

    filterFile = open("C:/Users/{}/Documents/BranchCompareOutput/Filtered/{}.txt".format(userName, filterFileName), 'w')

    temp1 = open("C:/Users/{}/Documents/BranchCompareOutput/Filtered/temp1.txt".format(userName), 'w')

    filterPath = input("Please enter the path you would like to filter: ")

    filterPath = "C:/Dev/CoreFW/" + filterPath

    lines = allBranchContent.split('\n')

    index = 0

    for line in lines:

        if '-' in line:
            if filterPath in line:
                temp1.write(line+'\n')
        elif '+' in line:
            if filterPath in line:
                temp1.write(line+'\n')
        else:
            temp1.write(line+'\n')

        index += 1

    temp1.close()
    temp2 = open("C:/Users/{}/Documents/BranchCompareOutput/Filtered/temp1.txt".format(userName), 'r')
    temp3 = open("C:/Users/{}/Documents/BranchCompareOutput/Filtered/temp3.txt".format(userName), 'w')
    temp1Content = temp2.read()
    lines = temp1Content.split('\n')
    index = 0

    for line in lines:
        if '<' in line:
            if '-' in lines[index+1]:
                temp3.write(line+'\n')
            elif '+' in lines[index+1]:
                temp3.write(line+'\n')
        
        # elif '#' in line:
        #     if ''

        else:
            temp3.write(line+'\n')

        index += 1

    temp3.close()
    temp4 = open("C:/Users/{}/Documents/BranchCompareOutput/Filtered/temp3.txt".format(userName), 'r')
    temp3Content = temp4.read()
    lines = temp3Content.split('\n')
    index = 0

    for line in lines:
        if "#" in line:
            #print(line)
            for i in range(10):
                if '<' in lines[index+i]:
                    j = 0
                    # control = 0
                    # while j < 3:
                    #     if lines[index+j] == "":
                    #         print(lines[index+j])
                    #     else:
                    #         filterFile.write(lines[index+j] + '\n')
                    #         print(lines[index+j])
                    #         j += 1

                    #     if j > 3:
                    #         break

                    filterFile.write(lines[index] + '\n')
                    print(lines[index])
                    
                    break
        elif '~' in line:
            index += 1
        elif '=' in line:
            index += 1
        else:
            filterFile.write(line+'\n')
        
        index += 1

        

    temp1.close()
    temp2.close()
    temp3.close()
    temp4.close()
    filterFile.close()

    os.remove("C:/Users/Rolando/Documents/BranchCompareOutput/Filtered/temp1.txt")
    os.remove("C:/Users/Rolando/Documents/BranchCompareOutput/Filtered/temp3.txt")


    


    print("")
    print("FINISHED")
    print("{} saved in C:/Users/{}/Documents/BranchCompareOutput/Filtered/{}.txt".format(filterFileName, userName, filterFileName))
    print("")
    print("Press Enter to return to Main Menu")

