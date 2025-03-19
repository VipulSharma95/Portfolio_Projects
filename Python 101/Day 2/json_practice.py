import json
from hello_frieda import dog_data

#Dump to JSON
food_ratings = {'organic dog food':2,"human food":10}
print(json.dumps(food_ratings))

data = {"name": "Vipul", "age": 29}
with open("data.json", "w") as file:
    json.dump(data, file)

numbers_present = {1: True, 2: True, 3: False}
print(json.dumps(numbers_present))

dog_id = 1
dog_name = "Frieda"
dog_registry = {dog_id: {"name":dog_name}}
dog_json = json.dumps(dog_registry)
print(json.dumps(dog_registry))

available_nums = {(1, 2): True, 3: False}
print(json.dumps(available_nums, skipkeys=True))

toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
print(json.dumps(toy_conditions, sort_keys=True))

#json.loads() and json.load()
new_dog_dictionary = json.loads(dog_json)
print(new_dog_dictionary==dog_registry)

with open("hello_frieda.json", mode = "r", encoding = "utf-8") as read_file:
    frie_data = json.load(read_file)

print(type(frie_data))
print(frie_data["name"])

print(type(frie_data["address"]["home"]))
print(type(dog_data["address"]["home"]))



