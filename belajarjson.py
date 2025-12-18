# import json
# data = {
#     "employees":[
#         {
#             "firstname":"jhon",
#             'lastname':'doe'},
#         {
#             'firstname':'mike',
#             'lastname':'schmidt'
#         },
#         {
#             'firstname':'peter',
#             'lastname':'parker'
#         }
#     ]    
# }
# print(type(data))
# with open("data_file.json","w") as file:
#     json.dump(data, file, indent=4)
# print(json.dumps(data, indent=4))
# deserialize
# import json
# json_string = """{
#     "firstname": "fanny",
#     "lastname": "lorenz",
#     "city": "shigatse",
#     "country": "senegal",
#     "countrycode": "no",
#     "email": "fanny_lorenz@gmail.com"
#     }
# """
# python_dict = json.loads(json_string)

# print(python_dict['firstname'])
# print(python_dict['lastname'])
# with open('json_file.json','r') as file:
    # python_dict = json.load(file)
print(type(python_dict))
print(python_dict)
print(python_dict['country'])
print(python_dict['email'])