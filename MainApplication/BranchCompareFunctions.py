from distutils.dir_util import copy_tree
import os
import filecmpModified
import subprocess
import getpass

userName = getpass.getuser()
repoContainerPath = "C:/Dev"
gitRepoPath = "C:/Dev/CoreFW"
#gitRepoPath = "C:/Users/Rolando/Desktop/Git Repos/testgitapi"

def branchTitlePrint(title):
    title = os.path.basename(title)
    print('############' + title + '############', file=f)
    print("", file=f)

def changeToForwardSlash(path):
        return path.replace('\\', '/')


def setupBranchComparison(isCoreFW):
    #instantiate .txt file
    global f
    f = open("C:/Users/{}/Documents/BranchCompareOutput/AllBranches/BranchCompareAllCoreFW.txt".format(userName), 'w')
    print(".txt file created")

    if (isCoreFW):
        repoContainerPath = "C:/Dev"
        gitRepoPath = "C:/Dev/CoreFW"
    else:
        gitRepoPath = input("Please enter the path location of the Repository on your computer: ")
        gitRepoPath = changeToForwardSlash(gitRepoPath)
        repoContainerPath = os.path.dirname(gitRepoPath)

    os.chdir(gitRepoPath)

    #Ensure Master Branch is checked out
    os.system('git checkout master')
    os.system('git branch')

    #Make a copy of the Master Branch (to use fore comparison)
    global masterBranchCopyPath
    masterBranchCopyPath = repoContainerPath + "/masterCopy"
    if os.path.isdir(masterBranchCopyPath):
        print("No copying of Master Branch needed")
    else:
        print("Copying Master...")
        copy_tree(gitRepoPath, masterBranchCopyPath)
        print('Master Branch Copied')

    #Create list of branches
    stdout = subprocess.check_output('git branch -a'.split())
    out = stdout.decode()
    global branches
    branches = [b.strip('* ') for b in out.splitlines()]

def runBranchComparison():
    print("There are {} branches to compare".format(len(branches)-1))
    print()
    print()
    input("Press Enter to start comparison process")
    # print()
    # print()
    # print()

    #Loop for comparison
    for i in range(len(branches)): #range(len(branches))
        if branches[i] == "master": #skip master Branch
            print("Skipped Master Branch from comparing to itself")
            continue
        else:
            os.system('git fetch')          #fetch for remote checkout
            os.system('git checkout ' + branches[i]) #checkout current branch
            
            featureBranchPath = gitRepoPath #make a Branch path to pass in just incase
            # featureBranchPath = "C:/Dev/CoreFW/Tools/Firmware/"
            # masterBranchCopyPath = "C:/Dev/masterCopy/Tools/Firmware/"

            # featureBranchPath = "C:/Users/Rolando/Desktop/Git Repos/testgitapi"
            # masterBranchCopyPath = "C:/Dev/masterCopyTestGit"
            

            branchComparison = filecmpModified.dircmp(masterBranchCopyPath, featureBranchPath) #instantiate Comparison object with desired paths (always compare to master in this case)
            branchComparison.report_full_closure() #run full closure method from modified filcmp library

            branchTitlePrint(branches[i]) #Print branch header
            print(branchComparison.outReport(f)) #print report to file

            print("Branches complete: {}/{}".format(i+1,len(branches)-1))

    f.close()
    print("")
    print("")
    print("")
    print("")
    print("FINISHED")
    print("BranchCompareAll saved in C:/Users/{}/Documents/BranchCompareOutput/AllBranches/BranchCompareAll.txt".format(userName))
    print("")
    input("Press Enter to return to Main Menu")

