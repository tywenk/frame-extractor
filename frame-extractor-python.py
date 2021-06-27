from typing import NewType
import cv2
import sys
import glob
import os

# source images directory
dirPath = str(sys.argv[1])
increment = int(sys.argv[2])


os.chdir(dirPath)

types = ('*.mov', '*.mp4')  # the tuple of file types
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))


for file in files_grabbed:

    fileD = os.path.splitext(file)[0]

    newpath = f"{dirPath}\{fileD}"

    print(file)

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    print(f"Pulling frames from {file}")
    cap = cv2.VideoCapture(f"{dirPath}\{file}")
    count = 0

    while cap.isOpened():

        ret, frame = cap.read()

        if ret:
            loc = f"{newpath}/"
            cv2.imwrite(f"{loc}{fileD}-frame{count}.jpg", frame)
            count += increment
            cap.set(1, count)
            print("Getting frame " + str(count))
        else:
            cap.release()
            break

    if cap.isOpened() == False:
        print("Finsished")
