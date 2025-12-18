import requests
import json
api_url = "https://restcountries.com/v3.1/capital/jakarta"
response = requests.get(api_url)
print(type(response))
print(response)
data = response.json()
for todo in data:
   
        json_object = json.dumps(todo, indent=3, ensure_ascii=False)
        print(json_object)