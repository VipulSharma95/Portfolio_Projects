from sqlalchemy.dialects.mysql.base import MySQLDialect

my_list = [1,2,3]
my_list2 = ["a","b","c"]

my_list3= ["a",1,"Python",5]

my_nested_list = [my_list,my_list2]
print(my_nested_list)

#extend list
my_list2.extend(my_list3)
print(my_list2)

#or

extended_list = my_list2+my_list3
print(extended_list)

#casting

list1 = [1,2,3]
tup1 = tuple(list1)
print(tup1)
print(type(tup1))

my_dict = {"name":"Vipul", "age":29}
print("name" in my_dict)
print("subject" in my_dict)

print("name" in my_dict) #fast
print("name" in my_dict.keys()) #slow
