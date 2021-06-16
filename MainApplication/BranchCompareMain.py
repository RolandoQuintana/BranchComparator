from distutils.dir_util import copy_tree
import os
import filecmpModified
import subprocess
import getpass
import mainMenuFunctions


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
userName = getpass.getuser()

###Menu###
if not os.path.isdir("C:/Users/{}/Documents/BranchCompareOutput".format(userName)):
    os.mkdir("C:/Users/{}/Documents/BranchCompareOutput".format(userName))
    os.mkdir("C:/Users/{}/Documents/BranchCompareOutput/Filtered".format(userName))
    os.mkdir("C:/Users/{}/Documents/BranchCompareOutput/AllBranches".format(userName))

mainMenuFunctions.main()
























