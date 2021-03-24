import json 
import urllib
from datetime import date 
import requests
def get_prayers(lat,lng,method,date):
	url = f"http://api.aladhan.com/v1/timings/{str(date)}?latitude={str(lat)}&longitude={str(lng)}&method={str(method)}"
	url_data = urllib.request.urlopen(url)
	json_data = json.loads(url_data.read())
	json_data_1 = json_data["data"]
	json_data_2 = json_data_1["timings"]
	return json_data_2


prayers = get_prayers(30,31,5,date.today())
for prayer in prayers :
	print(f"{prayer} : {prayers[prayer]}")
input("press enter to exit")