# pip3 install requests==2.31.0
import requests

url = "https://api.github.com"
response = requests.get(url)
print(f"HTTP request to {url}, returned status code: {response.status_code}")