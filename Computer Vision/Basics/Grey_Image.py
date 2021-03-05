import cv2
image = cv2.imread("sample2.jpg")
greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png', greyImage)
cv2.imshow("Color_image",image)
cv2.imshow("Grey_image", greyImage) 
cv2.waitKey(0)
cv2.destroyAllWindows()

