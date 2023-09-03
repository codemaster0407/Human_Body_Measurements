

import base64
import io
import os
import requests

url = "https://background-removal.p.rapidapi.com/remove"

payload = {
	"image_url": "https://objectcut.com/assets/img/raven.jpg",
	"output_format": "base64",
	"to_remove": "background"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "1f880f30b0msh2fe1b0ddc62d660p1f3885jsn31875a0ee477",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

# print(response.json())

output = response.json()
# print(response.json())


import base64
import io
import os



# Decode the base64 string to bytes
image_bytes = base64.b64decode(output['response']['image_base64'])

# Specify the path and filename for the output .png file
output_path = "output.png"

# Write the bytes to a .png file
with open(output_path, "wb") as file:
    file.write(image_bytes)

print(f"Image saved as {output_path}")
