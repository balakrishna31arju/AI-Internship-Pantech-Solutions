import cv2
import time
import json
import base64
import urllib.request
import imutils
import requests
import numpy as np
from authKey import SECRET_KEY


def camera():
    url = "http://100.67.9.178:8080/shot.jpg"
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    img = imutils.resize(img, width=600)
    cv2.imshow("frame", img)
    return img


while True:

    img = camera()
    key = cv2.waitKey(1) & 0xff
    if (key == ord('q')):
        cv2.destroyAllWindows()
        print("Captured...")
        cv2.imwrite("first.jpg", img)
        time.sleep(5)
        IMAGE_PATH = 'first.jpg'
        with open(IMAGE_PATH, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())
        url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=in&secret_key=%s' % (SECRET_KEY)
        r = requests.post(url, data=img_base64)

        num_plate = (json.dumps(r.json(), indent=2))
        info = (list(num_plate.split("candidates")))
        print(info)
        plate = info[1]
        plate = plate.split(',')[0:3]
        p = plate[1]
        p1 = p.split(":")
        number = p1[1]
        number = number.replace('"', '')
        number = number.lstrip()
        print(number)

        if number == "TN57AD3604":
            print("----------------------------")
            print("Owner Name: KANNA")
            print("Vehicle Number: %s" % number)
            print("Address: Chennai")

    elif key == 27:
        break

cv2.destroyAllWindows()
