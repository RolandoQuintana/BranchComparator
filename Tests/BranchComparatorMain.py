import os
import filecmpModified
from posixpath import relpath
import pathlib



# homeDir = os.system("cd ~")
# print("'cd ~' ran with exit code %d" %homeDir)
# unknownDir = os.system("cd doesnotexist")
# print("'cd doesnotexist' ran with exeit cod %d" %unknownDir)

#################################################
#           TEST AT WORK        #

path = '/Users/Rolando/Downloads/'
pathBranch = '/Users/Rolando/Downloads/Test-Repository-testBranch1'
pathMaster = '/Users/Rolando/Downloads/Test-Repository-main'

################################################


##################################################
#           Test AT HOME            #

# path = '/Users/danie/Downloads/'
# pathBranch = '/Users/danie/Downloads/Test-Repository-testBranch1'
# pathMaster = '/Users/danie/Downloads/Test-Repository-main'

###################################################
# comparison = filecmp.dircmp(path+'Test-Repository-testBranch1', path +'Test-Repository-main')
# common_files = ', '.join(comparison.common)
# leftOnlyFiles = ', '.join(comparison.left_only)
# rightOnlyFiles = ', '.join(comparison.right_only)
# with open(path+'folder_diff.txt', 'w') as folderReport:
#     folderReport.write("Common Files: "+common_files+'\n')
#     folderReport.write('\n'+ "Only in feature Branch: "+ leftOnlyFiles+'\n')
#     folderReport.write('\n'+ "Only in main branch: " + rightOnlyFiles+ '\n')



dirComparison = filecmpModified.dircmp(pathMaster, pathBranch)
dirComparison.report_full_closure()

with open(path+'BranchCompare.txt', 'w') as branchReport:
    branchReport.write("###############################"+'\n')
    branchReport.write("Test-Repsitory-testBranch1"+'\n')
    branchReport.write("###############################"+'\n')
    branchReport.write("")
    branchReport.write("")

    branchReport.write(dirComparison.outReport())



# print("###############################")
# print("Test-Repository-testBranch1")
# print("###############################")
# print()
# print()

# # dirComparison = filecmpModified.dircmp(pathMaster, pathBranch)


# dirComparison.report_full_closure()
# print(dirComparison.outReport())

