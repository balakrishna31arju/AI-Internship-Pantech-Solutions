import json
import base64
import requests
from authKey import SECRET_KEY

IMAGE_PATH = '9.jpeg'


with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=in&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

num_plate=(json.dumps(r.json(), indent=2))
info=(list(num_plate.split("candidates")))
print(info)
plate=info[1]
plate=plate.split(',')[0:3]
p=plate[1]
p1= p.split(":")
number=p1[1]
number=number.replace('"','')
number=number.lstrip()
print (number)

if number == "KL32L5050":
    print("----------------------------")
    print("Owner Name: Arjun")
    print("Vehicle Number: %s"%number)
    print("Address: KARNATAKA")
