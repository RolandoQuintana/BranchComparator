import os
import subprocess
from distutils.dir_util import copy_tree

print("Hello World")
#print(os.system('Get-Location'))
os.system('cd')
os.chdir('..')
os.mkdir('testCopy')

fromDirectory = '/Users/Rolando/Desktop/Git Repos/testgitapi'
toDirectory = '/Users/Rolando/Desktop/Git Repos/test'

copy_tree(fromDirectory, toDirectory)