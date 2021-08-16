import requests
import json 

url = "https://pokeapi.co/api/v2/pokemon/6/"

r = requests.get(url)

data = r.json()

print(json.dumps(data))
