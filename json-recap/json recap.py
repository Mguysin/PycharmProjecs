import json

car = {'engine': 'electric',
       'brand': 'Tesla',
       'type-reques': 'DELETE'}

print(type(car))


# json.dumps(obj-dict-json) --> str
print(type(json.dumps(car)))




#Saving/creating/encoding JSON
# json.dump(obj, path) --> file with text formatted as json

       #path needs to be created using the open() built in function
with open('example', 'w') as amazing_path_to_json:
       json.dump(car, amazing_path_to_json)





# Opening/loading/decoding Json
with open('example') as json_file_to_load:
       json_loaded_objt = json.load(json_file_to_load)
       print(json_loaded_objt)
       print(type(json_loaded_objt))
       for key in json_loaded_objt:
              print('This is a key', key)
              print('This is a value', json_loaded_objt[key])
