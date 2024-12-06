import cv2 as cv
import sys

#Function to Read image imread(filename, dst|flags)
img = cv.imread("./data/lena.jpg")
 
if img is None:
    sys.exit("Could not read the image.")
 
cv.imshow("Display window", img)
k = cv.waitKey(0)
 
if k == ord("s"):
    cv.imwrite("starry_night.png", img)