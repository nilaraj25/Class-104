import cv2

#reading the image
img = cv2.imread("butterfly.jpg")

#displaying the colored image
cv2.imshow("Display Image", img)

#convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#displaying grayscale image
cv2.imshow("Grayscale",gray_img)

#will be infinite time (if number is given, it will be there for that amount of time(0 means infinite))
cv2.waitKey(0)

