import requests
import time
url = "http://192.168.112.242/saved-photo"
# requests.get("http://192.168.112.242/capture")
time.sleep(1)
response = requests.get(url)

with open("image1.jpg", "wb") as f:
    f.write(response.content)
