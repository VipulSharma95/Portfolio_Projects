#List Comprehension
x = [i for i in range(5)]
print(x)

x = ['1','2','3','4','5']
y = [int(i) for i in x]
print(y)

vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])

#Dictionary Comprehension

my_dict = {1:'dog', 2:'cat', 3:'mouse'}
print({value:key for key,value in my_dict.items()})

my_list1 = [1,1,2,2,3,4,5,6,7,7,8]
my_set = {x for x in my_list1}
print(my_set)
