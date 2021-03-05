import cv2
import time
import imutils

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def recText(img):
    text = pytesseract.image_to_string(img)
    return text


cam = cv2.VideoCapture(0)
time.sleep(1)

while True:
    _, img = cam.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = "Normal"
    img = imutils.resize(img, width=500)

    cv2.imshow("Camera Feed", img)
    key = cv2.waitKey(1)
    if key == 27:
        info = recText(img)
        print(info)
        break

cv2.imshow("Camera Feed", img)
cam.release()