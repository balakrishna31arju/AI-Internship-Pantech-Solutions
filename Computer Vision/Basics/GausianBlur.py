import cv2
img = cv2.imread("sample.jpg")
GaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("GaussianBlurImage.jpg", GaussianBlurImg)
