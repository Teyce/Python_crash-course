# A List is a collection which is ordered and changeable. Allows duplicate members.
#create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes', 'pears']

#use a constructor
# numbers2 = list((1, 2, 3, 4, 5))
# print (fruits[1])
# print(numbers, numbers2)

#get length
# print(len(fruits))

#append to list
fruits.append('carrots')

#remove from list
fruits.remove('grapes')

#Insert into position
fruits.insert(2, 'strawberries')

#Insert with pop
fruits.pop(2)
#Reverse and sort
fruits.sort()
fruits.reverse()

fruits.sort(reverse= True)
fruits[0] = 'blueberries'
print(fruits)

