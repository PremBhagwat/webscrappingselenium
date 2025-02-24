import requests
import os

def fetchAndSaveToFile(url, path):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:

        f.write(r.text)

url= "https://www.dell.com/en-in/search/laptop"

fetchAndSaveToFile(url, "data/dell.html")
