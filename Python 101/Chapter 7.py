my_dict = {"a":1,"b":2,"c":3}
try:
    value=my_dict["d"]
except KeyError:
    print("This key does not exist")


my_dict = {"a":1,"b":2,"c":3}
try:
    value=my_dict["d"]
except KeyError:
    print("This key does not exist")
finally:
    print("The code is complete")

my_dict = {"a":1,"b":2,"c":3}
try:
    value=my_dict["b"]
except KeyError:
    print("This key does not exist")
else:
    print("No Error found.")