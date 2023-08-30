import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"} ## location currently set to boston

headers = {
	"X-RapidAPI-Key": "653d55c5a8mshf7c312e8a46d46ap152195jsn16c8aa3dde4d",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())