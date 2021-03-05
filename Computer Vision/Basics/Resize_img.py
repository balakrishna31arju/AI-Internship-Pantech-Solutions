import cv2
import imutils
img = cv2.imread("sample.jpg")
resizeImg = imutils.resize(img, width = 500)
cv2.imwrite("ResizedImage.jpg", resizeImg)
