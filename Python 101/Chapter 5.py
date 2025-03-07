for number in range(5):
    print(number)

a_dict = {1:"one",2:"two",3:"three",4:"four",5:"five"}
keys = a_dict.keys()
keys = sorted(keys)

for key in keys:
    print(key)

i=0
while i<10:
    print(i)
    if i==5:
        break
    i+=1

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 10:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")
