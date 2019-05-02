import json
car = {'engine': 'electric', 'brand': 'Tesla'}




s_car = json.dumps(car)

print(s_car)
print(type(s_car))



with open('new_json_car_file', 'w') as jsonfile:
    json.dump(car, jsonfile)

