import json
with open('tugasjson.json','r', encoding="utf-8") as file:
    python_dict = json.load(file)
    print(type(python_dict))
    print(python_dict[0]['name']['common'])
    print(python_dict[0]['capital'][0])