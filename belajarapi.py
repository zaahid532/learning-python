# import requests
# import json
# api_url = "https://jsonplaceholder.typicode.com/todos"
# response = requests.get(api_url)
# print(type(response))
# print(response)
# data = response.json()
# for todo in data:
#     if todo['completed'] == True:
#         json_object = json.dumps(todo, indent=3)
#         print(json_object)
import requests
apikey = '4243b23c41baffc449a500ce1cddc43a'
city = 'jakarta'
countrycode = 'ID'
api_url = (
    'https://api.openweathermap.org/data/2.5/weather?'
    +'q=' + city + ',' + countrycode
    +'&appid=' + apikey
    +'&units=metric'
    +'&lang=id'
)

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    nama_kota = data['name']
    suhu = data['main']['temp']
    kelembaban = data['main']['humidity']
    cuaca = data['weather'][0]['description']
    angin = data['wind']['speed']
    print("cuaca di", nama_kota)
    print('suhu         :', suhu, '°C')
    print('kelembaban   :', kelembaban, '%')
    print('kondisi      :', cuaca)
    print("kecepatan angin:", angin, "m/s")
else:
    print('gagal mengambil data cuaca')
    print("status code:", response.status_code)