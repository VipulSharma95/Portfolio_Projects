string_1 = "Hello World"
string_2 = 'Hello World'
string_multi_line = '''
This is a multi line string'''

my_num = 123
my_string_from_num = str(my_num)

# = int('ABC') #Error - Type Conversion
y = int('123')  # Works Fine

my_string = "abc"
# my_string[0] = "d" # Error - String is immutable - Type Error

# String concatenation
str_1 = "My dog ate "
str_2 = "my homework"
str_3 = str_1 + str_2
print(str_3)

#String methods
my_string = "this is a string!"

print(my_string.upper())
print(my_string.capitalize())

print(my_string[0:2])

#String formatting

my_string = "I like %s" % "Python"
print(my_string)

my_string = "%i + %i = %i" % (1,2,3)
print(my_string)

float_string = "%f" % (1.23765)
print(float_string)

float_string_2 = "%.2f" % (1.23765)
print(float_string_2)

#New formatting
print("%(lang)s is fun!" % {'lang':'Python'})

#Formatting using format
print("Python is as simple as {0} {1} {2}".format("a","b","c"))


