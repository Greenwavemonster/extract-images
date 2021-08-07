import os
import shutil
from pathlib import Path

# By Greenwavemonster :)
# WIP

def userIn():
    global startDir
    global endDir
    global fileEnd

    print("Enter full Path to Dir from which you want to extract files (C:\\Users\\Greenwave\\FolderX\\FolderY): ")
    while True:
        startDir = input()
        if os.path.exists(startDir):
            print("Enter the full Path to where you want the files to be (C:\\Users\\Greenwave\\destination): ")
            while True:
                endDir = input()
                if os.path.exists(endDir):
                    print("Enter file ending (with dot!) [.png, .jpg, .txt, .jpeg]: ")
                    while True:
                        fileEnd1 = input()
                        if fileEnd1.startswith('.'):
                            fileEnd = fileEnd1
                            break
                        else:
                            fileEnd = '.' + fileEnd1
                            break
                    break
                print("Seems not like a valid Destination... Try again: ")
            break
        print("Not a valid Path... Try again: ")


path1 = r"C:\Users\Greenwave\PycharmProjects\instaread"

def scanEndings(): # This will go into all childfolders to look for images --> .jpg is not changed
    for users in os.listdir(path1):
        for image in Path(r'C:\Users\Greenwave\PycharmProjects\instaread', users).glob("*.jpg"):
            print(image)
            createFolders(users, image)


def createFolders(users, image): #It will create a new folder with the same new in the new Directory (Dir should be created if not existent)
    folderPath = os.path.join(r'C:\Users\Greenwave\Desktop\projectFiles-sorted', users)
    #print(folderPath)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    else:
        print("User Exists...")

    moveImg(folderPath, image)


def moveImg(folderPath, image): # Copys things
    shutil.copy(image, folderPath)
    print("Image has been Copied...")


# === START ===
print("Start")
scanEndings()
