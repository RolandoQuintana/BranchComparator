import os
import subprocess
from distutils.dir_util import copy_tree
#import path

mainDirectory = '/Users/Rolando/Desktop/Git Repos'
fromDirectory = '/Users/Rolando/Desktop/Git Repos/testgitapi'
os.system('cd')
#print(os.system('Get-Location'))
os.chdir(fromDirectory)
os.system('cd')
os.system('git checkout master')
os.system('git branch')
os.system('dir')
#os.mkdir('testCopy')


toDirectoryMasterCopy = '/Users/Rolando/Desktop/Git Repos/testgitapiMasterCopy'
toDirectoryTestBranch1Copy = '/Users/Rolando/Desktop/Git Repos/testgitapiTestBranch1Copy'

delFeaturePath = toDirectoryTestBranch1Copy.replace('/','\\')

print(delFeaturePath)

copy_tree(fromDirectory, toDirectoryMasterCopy)

os.system('git fetch')
os.system('git checkout Branch1')
os.system('git branch')
os.system('dir')
copy_tree(fromDirectory, toDirectoryTestBranch1Copy)

input("REady to move on?")

#os.system('del -rf ' + toDirectoryMasterCopy)
#os.system('del -rf ' + delFeaturePath)

#os.system('"' + 'del -rf ' + delFeaturePath + '"')
#os.system(deleteCommand)
os.chdir(mainDirectory)
subprocess.call('del -rf ' + delFeaturePath)

