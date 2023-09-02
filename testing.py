import requests
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"London","days":"3"}

headers = {
    "X-RapidAPI-Key": "653d55c5a8mshf7c312e8a46d46ap152195jsn16c8aa3dde4d",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

answer = (response.json())["forecast"]["forecastday"]

daylist = []

## I only have the free use of the api, which only allows me to use a 3 day forecast.
## Otherwise, api call can call up to 14 days for forecast.
for i in range(0,2):

    daylist.append({
        "date": answer[i]["date"],
        "maxtempf": answer[i]["day"]["maxtemp_f"],
        "maxtempc": answer[i]["day"]["maxtemp_c"],
        "mintempf": answer[i]["day"]["mintemp_f"],
        "mintempc": answer[i]["day"]["mintemp_c"],
        "avgtempf": answer[i]["day"]["avgtemp_f"],
        "avgtempc": answer[i]["day"]["avgtemp_c"],
        "weather": answer[i]["day"]["condition"]["text"],
        "weather": answer[i]["day"]["condition"]["icon"]
    })

print(daylist)
print(answer[0]["day"])
