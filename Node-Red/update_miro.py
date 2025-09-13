import requests
import sys
import json


base_url = "https://api.miro.com/v2/boards/uXjVJI5TngI%3D"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJtaXJvLm9yaWdpbiI6ImV1MDEifQ_jIa2JF6rf_3VN2zF8_TFoJDnWJs"
}

url2 = "/images"
payload2 = { "data": { "url": sys.argv[1] },"position": {
        "x": 100,
        "y": -45
    } }

response2 = requests.post(base_url + url2, json=payload2, headers=headers)


print(response2.text)

#grupo 1 id 3458764603121872259
