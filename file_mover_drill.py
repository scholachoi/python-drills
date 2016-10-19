"""
Title:File Mover Drill
Scenario: Your employer wants a program to move all his .txt files from one
folder to another with the click of a button. On your desktop make 2 new folders:
Folder A and Folder B. Create 4 random .txt files and put them in Folder A.
Plan:
-Move the files from Folder A to folder B
-Print out each file path that got moved onto the shell
-After execution, the moved files should not be in Folder A
Guidelines:
-Use Python 2.7x
-Import shutil module
-Run it on the Python shell
-Use IDLE
"""

import shutil
import os

folderA = 'C:/Users/Student/Desktop/FolderA/'
folderB = 'C:/Users/Student/Desktop/FolderB/'

filesinA = os.listdir(folderA)

for file in filesinA:
    shutil.move(folderA+file, folderB)
    print os.path.realpath(folderB+file)


        



    
