# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
# import json
# ##Sample Json( outside api)
# userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'
# #We want to parse this into a dictionary
# user = json.loads(userJSON)
# # print(user['first_name'])
# print(user)

###Converting dict to json# print(carJSON)
import json
milkJSON = '{"name": "fresha", "brand": "whole", "size": 30}'
milk = json.loads(milkJSON)
# print(milk)
# print(milk["name"])

#3 dict into JSON
milk = {'name': 'fresha', 'brand': 'whole', 'size': 30}
milkJSON = json.dumps(milk)
print(milkJSON)