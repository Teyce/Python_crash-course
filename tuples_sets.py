# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

fruits = ('oranges', 'mangoes', 'apples')
# get a value
print(fruits[1])

#can't change values
#but can be deleted
# del fruits2
# print(fruits2)

# get length of fruits
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
# create a tuple
# a set is created with curly braces
#create a set
fruits_set = {'oranges', 'mangoes', 'apples'}
# print(fruits_set)

# check if in set
# print('apples' in fruits_set)

# add to a set
fruits_set.add('carrots')
#remove from set
# fruits_set.remove('carrots')
# # clear and delete set
# fruits_set.clear()
# del fruits_set
print(fruits_set)