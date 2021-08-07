import os
import shutil
from pathlib import Path

# By Greenwavemonster :)

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
