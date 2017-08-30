"""
Title:File Mover
Scenario: An employer wants a program to move all .txt files from one
folder to another with the click of a button. 
What the program does:
-Move the files from Folder A to folder B
-Print out each file path that got moved onto the shell
Requirements:
-Use Python 2.7x
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


        



    
