# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#create dictionary; with key pairs with quotes
person = {
'first_name': 'John',
'last_name': 'Doe',
'age': 30
}
# print(person, type(person))

# get a value
# print(person['first_name'])
# print(person.get('last_name'))

#add key/value
person['phone'] = '000-000-000'
# print(person)

#get dict keys
# print(person.keys())

#get items
# print(person.items())

# copy dict
person2 = person.copy()
# print(person2)

person2['city'] = 'Boston'
# print(person2)

del(person['age'])
person.pop('phone')
person.clear()
# print(len(person2))

#list of dict
people = [
    {'name': 'Amos', 'Age': 30},
    {'name': 'Jane', 'Age': 20}
]
print(people[0] ['name'])
