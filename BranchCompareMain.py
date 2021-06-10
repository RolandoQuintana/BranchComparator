from distutils.dir_util import copy_tree
import os
import filecmpModified
import subprocess


######################################
'''
This Script is design to compare the branches with the master branch
of a gitlab repo.

'''
######################################

# def branchTitlePrint(title):
#     print("############")
#     print(title)
#     print("############")
#     print("")

def branchTitlePrint(title):
    print("############", file=f)
    print(title, file=f)
    print("############", file=f)
    print("", file=f)


userName = input("Please enter computer User Name: ")

#instantiate .txt file
f = open("C:/Users/{}/Desktop/BranchCompare.txt".format(userName), 'w')

######Obtain Repo Path & change to this path directory#####

#test
repoContainerPath = "C:/Users/Rolando/Desktop/Git Repos/"
gitRepoPath = "C:/Users/Rolando/Desktop/Git Repos/testgitapi" 

#coreFw
# repoContainerPath = "C:/Dev"
# gitRepoPath = "C:/Dev/CoreFW" 

os.chdir(gitRepoPath)

#Ensure Master Branch is checked out
os.system('git checkout master')

#Make a copy of the Master Branch (to use fore comparison)
masterBranchCopyPath = repoContainerPath + "/masterCopy"
copy_tree(gitRepoPath, masterBranchCopyPath)

#Create list of branches
branches = os.listdir('.git/refs/heads')

#Loop for comparison
for i in range(len(branches)):
    if branches[i] == "master": #skip master Branch
        continue
    else:
        os.system('git fetch')          #fetch for remote checkout
        os.system('git checkout ' + branches[i]) #checkout current branch
        
        featureBranchPath = gitRepoPath #make a Branch path to pass in just incase

        branchComparison = filecmpModified.dircmp(masterBranchCopyPath,featureBranchPath) #instantiate Comparison object with desired paths (always compare to master in this case)
        branchComparison.report_full_closure() #run full closure method from modified filcmp library

        branchTitlePrint(branches[i]) #Print branch header
        print(branchComparison.outReport(f)) #print report to file







