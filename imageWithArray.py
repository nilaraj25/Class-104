import numpy as mp
import cv2

black=mp.zeros([600, 600])

black[200:400, 200:400]=255
print(black)

cv2.imshow("black", black)

cv2.waitKey(0)