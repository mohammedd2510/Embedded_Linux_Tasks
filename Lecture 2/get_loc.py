import requests
from pprint import pprint
response=requests.get("https://api.ipify.org/?format=json")
ip = response.json()["ip"]
response=requests.get(f"https://ipinfo.io/{ip}/geo")
loc = response.json()
pprint(loc)
