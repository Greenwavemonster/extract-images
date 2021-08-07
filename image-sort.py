import os
import shutil
from pathlib import Path


path1 = r"C:\Users\Max\PycharmProjects\instaread"

def scanEndings():
    # directories = os.listdir(path1)
    for users in os.listdir(path1):
        for image in Path(r'C:\Users\Max\PycharmProjects\instaread', users).glob("*.jpg"):
            print(image)
            createFolders(users, image)


def createFolders(users, image):
    folderPath = os.path.join(r'C:\Users\Max\Desktop\projectFiles-sorted', users)
    print(folderPath)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    else:
        print("User Exists...")

    moveImg(folderPath, image)


def moveImg(folderPath, image):
    shutil.copy(image, folderPath)
    print("Image has been Copied...")


# === START ===
print("Start")
scanEndings()
