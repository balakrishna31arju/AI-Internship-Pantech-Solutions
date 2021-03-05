import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://static.dezeen.com/uploads/2017/10/autohaus-matt-fajkus_dezeen_2364_sq1.jpg"}

headers = {
    'accept': "application/json",
    'authorization': "Basic xxxx"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(20):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
