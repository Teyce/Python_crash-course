# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# #concatenate

# print('Hello, My name is ' + name + str(age) + ' years ')


# String Formatting

# String Methods
# arguments by position
print('my name is {name} and i am {age}' .format(name=name, age=age))

s= 'hello world'
# capitalize strings
print(s.capitalize())
print(s.upper())
print(s.lower())