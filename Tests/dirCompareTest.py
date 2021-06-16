import filecmp
import os

# featureBranchPath = "C:/Dev/CoreFW/Tools/Firmware/"
# masterBranchCopyPath = "C:/Dev/masterCopy/Tools/Firmware/"

featureBranchPath = "C:/Users/Rolando/Desktop/Git Repos/testgitapi"
masterBranchCopyPath = "C:/Dev/masterCopyTestGit"

print(os.listdir(featureBranchPath))

for root, directories, files in os.walk(featureBranchPath, topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in directories:
        print(os.path.join(root, name))

# branchComparison = filecmp.dircmp(masterBranchCopyPath, featureBranchPath) #instantiate Comparison object with desired paths (always compare to master in this case)
# branchComparison.report_full_closure() #run full closure method from modified filcmp library

# os.chdir()
# os.listdir()




# def are_dir_trees_equal(dir1, dir2):
#     """
#     Compare two directories recursively. Files in each directory are
#     assumed to be equal if their names and contents are equal.

#     @param dir1: First directory path
#     @param dir2: Second directory path

#     @return: True if the directory trees are the same and 
#         there were no errors while accessing the directories or files, 
#         False otherwise.
#    """

#     dirs_cmp = filecmp.dircmp(dir1, dir2)
#     if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or \
#         len(dirs_cmp.funny_files)>0:
#         return False
#     (_, mismatch, errors) =  filecmp.cmpfiles(
#         dir1, dir2, dirs_cmp.common_files, shallow=False)
#     if len(mismatch)>0 or len(errors)>0:
#         return False
#     for common_dir in dirs_cmp.common_dirs:
#         new_dir1 = os.path.join(dir1, common_dir)
#         new_dir2 = os.path.join(dir2, common_dir)
#         if not are_dir_trees_equal(new_dir1, new_dir2):
#             return False
#     return True

# print(are_dir_trees_equal(masterBranchCopyPath, featureBranchPath))
