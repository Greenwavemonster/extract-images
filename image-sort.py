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

def scanEndings():
    for users in os.listdir(startDir):
        for image in Path(startDir, users).glob(fileEnd):
            print(image)
            createFolders(users, image)


def createFolders(users, image):
    folderPath = os.path.join(endDir, users)
    print(folderPath)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    else:
        print("User Exists...")  # Yes ik, this will print again and again...

    moveImg(folderPath, image)


def moveImg(folderPath, image):
    shutil.copy(image, folderPath)
    print("File has been Copied...")


# === START ===
print("=== Start ===")
userIn()
scanEndings()

