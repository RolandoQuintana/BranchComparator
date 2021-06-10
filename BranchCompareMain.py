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


print("___Welcome To Branch Compare___")
print("")
print("")
userName = input("Please enter computer User Name: ")

######Obtain Repo Path & change to this path directory#####


#test
# repoContainerPath = "C:/Users/Rolando/Desktop/Git Repos/"
# gitRepoPath = "C:/Users/Rolando/Desktop/Git Repos/testgitapi" 


#coreFw
repoContainerPath = "C:/Dev"
gitRepoPath = "C:/Dev/CoreFW" 



#instantiate .txt file
f = open("C:/Users/{}/Desktop/BranchCompare.txt".format(userName), 'w')
print(".txt file created")



os.chdir(gitRepoPath)
print("Directory Changed to: " + gitRepoPath)

#Ensure Master Branch is checked out
# os.system('git remote add origin http://gitlab.cirque.local/cirque/corefw.git')
# os.system('git pull origin master')
os.system('git checkout master')
os.system('git branch')

#Make a copy of the Master Branch (to use fore comparison)
masterBranchCopyPath = repoContainerPath + "/masterCopy"
if os.path.isdir(masterBranchCopyPath):
    print("No copying needed")
else:
    copy_tree(gitRepoPath, masterBranchCopyPath)
    print('Master Branch Copied')

input("Press Enter to Continue")

#Create list of branches
# branches = os.listdir('.git/refs/heads')
# input("Press enter to continue")
# for i in range(len(branches)):
#     print(branches[i])

stdout = subprocess.check_output('git branch -a'.split())
out = stdout.decode()
branches = [b.strip('* ') for b in out.splitlines()]
print(branches)

input("Press Enter to Continue")
print()
print()
print()

#Loop for comparison
for i in range(len(branches)):
    if branches[i] == "master": #skip master Branch
        print("Skipped Master Branch from comparing to itself")
        continue
    else:
        os.system('git fetch')          #fetch for remote checkout
        os.system('git checkout ' + branches[i]) #checkout current branch
        
        featureBranchPath = gitRepoPath #make a Branch path to pass in just incase

        branchComparison = filecmpModified.dircmp(masterBranchCopyPath,featureBranchPath) #instantiate Comparison object with desired paths (always compare to master in this case)
        branchComparison.report_full_closure() #run full closure method from modified filcmp library

        branchTitlePrint(branches[i]) #Print branch header
        print(branchComparison.outReport(f)) #print report to file

print("")
print("")
print("")
print("")
print("FINISHED")
input("Press enter to close")




