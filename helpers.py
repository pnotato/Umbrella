import requests
import json

## api return info from ddb

def weather(place):
	try:
		url = "https://weatherapi-com.p.rapidapi.com/current.json"
		querystring = {"q":place} ## location currently set to boston
		headers = {
			"X-RapidAPI-Key": "653d55c5a8mshf7c312e8a46d46ap152195jsn16c8aa3dde4d",
			"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers, params=querystring)
		response.raise_for_status()

		location = (response.json())["location"]
		current = (response.json())["current"]
		condition = (response.json())["current"]["condition"]

		return {
			"name": location["name"],
			"region": location["region"],
			"localtime": location["localtime"],
			"weather": condition["text"],
			"icon": condition["icon"],
			"celsius": current["temp_c"],
			"far": current["temp_f"],
			"windmph": current["wind_mph"],
			"windkph": current["wind_kph"],
			"percipmm": current["precip_mm"],
			"precipin": current["precip_in"],
			"humidity": current["humidity"],
			"cloud": current["cloud"]
		}

	except (requests.RequestException, ValueError, KeyError, IndexError):
		return None
