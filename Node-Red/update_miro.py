import requests
import sys
import json

url = "/shapes"

payload = {
    "data": { "shape": "rectangle" },
    "style": { "fillColor": "#ffffff" },
    "geometry": {
        "height": 500,
        "width": 400
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer "
}

response = requests.post(url, json=payload, headers=headers)


url2 = "/images"
payload2 = { "data": { "url": sys.argv[1] }, "geometry": {
        "width": 375
    },"position": {
        "x": 0,
        "y": -45
    } }

response2 = requests.post(url2, json=payload2, headers=headers)

url3 = "/shapes"
payload3 = {
    "data": { "content": sys.argv[2],"shape": "rectangle"},"style": { "fontSize": "14" },"geometry": { "width": 380,"height":90 }, "position": {
        "x": 2,
        "y": 190
    }}

response3 = requests.post(url3, json=payload3, headers=headers)
#print(sys.argv[1])
#print(sys.argv[2])

#convert string to  object

json_fondo = json.loads(response.text)
id_fondo = json_fondo["id"]


json_imagen = json.loads(response2.text)
id_imagen = json_imagen["id"]

json_texto = json.loads(response3.text)
id_texto = json_texto["id"]

print(id_fondo)
print(id_imagen)
print(id_texto)


url = "/groups"

payload = { "data": { "items": [id_fondo, id_imagen, id_texto] } }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer "
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
json_grupo = json.loads(response.text)
id_grupo = json_grupo["id"]


url = "/connectors"

#grupo 1 id: 3458764603121872259
#grupo 2 id : 3458764603159570539
#grupo 3 id: 3458764603161974720
#grupo 4 id: 3458764603162100083
#grupo 5 id : 3458764603162100313
#grupo 6 id: 3458764603162276355

temp_elgrupo = sys.argv[3]
elgrupo =""

if temp_elgrupo == "grupo1":
    elgrupo="3458764603121872259"
elif temp_elgrupo == "grupo2":
    elgrupo="3458764603159570539"
elif temp_elgrupo == "grupo3":
    elgrupo="3458764603161974720"
elif temp_elgrupo == "grupo4":
    elgrupo="3458764603162100083"
elif temp_elgrupo == "grupo5":
    elgrupo="3458764603162100313"
elif temp_elgrupo == "grupo6":
    elgrupo="3458764603162276355"

payload = {
    "startItem": { "id": elgrupo },
    "endItem": { "id": id_fondo }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer "
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

#grupo 1 id 3458764603121872259
