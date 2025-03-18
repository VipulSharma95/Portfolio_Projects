import json

food_ratings = {'organic dog food':2,"human food":10}
print(json.dumps(food_ratings))

numbers_present = {1: True, 2: True, 3: False}
print(json.dumps(numbers_present))

dog_id = 1
dog_name = "Frieda"
dog_registry = {dog_id: {"name":dog_name}}
print(json.dumps(dog_registry))

available_nums = {(1, 2): True, 3: False}
print(json.dumps(available_nums, skipkeys=True))

toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
print(json.dumps(toy_conditions, sort_keys=True))

