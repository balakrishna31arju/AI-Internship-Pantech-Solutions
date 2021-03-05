import numpy as np 
import cv2 
img = cv2.imread("sample1.png")
cv2.imshow("show",img) 
cv2.imwrite("photo.jpg",img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
