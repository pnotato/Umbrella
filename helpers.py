import requests
import json

## api return info from ddb

def weather(place):
	try:
		url = "https://weatherapi-com.p.rapidapi.com/current.json"
		querystring = {"q":place} ## location currently set to boston
		headers = {
			"X-RapidAPI-Key": "",
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
			"weather": condition["text"],
			"icon": condition["icon"],
			"celsius": current["temp_c"],
			"far": current["temp_f"],
		}

	except (requests.RequestException, ValueError, KeyError, IndexError):
		return None

## helper for background and text

def adjust(location):
	weather = location["weather"].lower()
	if "rain" in weather:
		return {
			"background": '/static/rainy.jpg',
			"advice": "You're gonna need that umbrella.",
			"text": "#5BC0DE"
		}

	elif weather == "clear" or weather == "sunny":
		return {
			"background": '/static/sunny.jpg',
			"advice": "Leave the umbrella at home.",
			"text": "#E89E3D"
		}
	elif "overcast" in weather or "cloud" in weather:
		return {
			"background": '/static/cloudy.jpg',
			"advice": "Bring the umbrella, just in case.",
			"text": "#E6D8B8"
		}
	else:
		return {
			"background": '/static/sunny.jpg',
			"advice": "Bring the umbrella, why not?",
			"text": "#A83131"
		}

## Forecast api

def forecastpredict(location):

	url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

	querystring = {"q":location,"days":"3"}

	headers = {
		"X-RapidAPI-Key": "",
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	answer = (response.json())["forecast"]["forecastday"]

	daylist = []

	## I only have the free use of the api, which only allows me to use a 2 day forecast.
	## Otherwise, the api call can call up to 14 days for forecast.


	for i in range(0,2):

		daylist.append({
			"date": answer[i]["date"],
			"avgtempf": answer[i]["day"]["avgtemp_f"],
			"avgtempc": answer[i]["day"]["avgtemp_c"],
			"weather": answer[i]["day"]["condition"]["text"],
			"icon": answer[i]["day"]["condition"]["icon"]
		})

	return daylist


