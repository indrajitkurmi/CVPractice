import numpy as np
import cv2 as cv

img1 = cv.imread("..\..\..\data\messi5.jpg")
assert img1 is not None, "file could not be read, check with os.path.exists()"

e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )

print("Print whether using optimized code",cv.useOptimized())

import timeit

