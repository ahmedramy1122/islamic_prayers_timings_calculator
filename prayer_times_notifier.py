import json 
import urllib
from datetime import date 
import requests
def get_prayers(lat=0,lng=0,method=5,date="01012021"):
	url = f"http://api.aladhan.com/v1/timings/{str(date)}?latitude={str(lat)}&longitude={str(lng)}&method={str(method)}"
	url_data = urllib.request.urlopen(url)
	json_data = json.loads(url_data.read())
	json_data_1 = json_data["data"]
	json_data_2 = json_data_1["timings"]
	return json_data_2
latitude = 0
longitude = 0
method = 0 
date = "000000000"
prayers = get_prayers(latitude,longitude,method,date)
for prayer in prayers :
	print(f"{prayer} : {prayers[prayer]}")
input("press enter to exit")
