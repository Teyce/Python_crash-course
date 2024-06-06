# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# for loop
# people = ['jane', 'Moses', 'Chris']
# for person in people:
#     print(f'current-person: {person}')


#Break
# people = ['jane', 'Moses', 'Anna', 'Christine', 'Chris']
# for person in people:
#  if person == 'Christine':
#    break
#  print(f'current-person: {person}')

# While loops execute a set of statements as long as a condition is true.

#Continue
people = ['jane', 'Moses', 'Ann', 'Christine', 'Chris']
for person in people:
 if person == 'Christine':
   continue
#  print(f'current-person: {person}')

 #Range
#  for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#   print(f'Number: {i}')

# #Trial
# fruits = ['orange', 'mango', 'apple']
# for fruit in fruits:
#   print(fruit)

# #for simple loop
# people = ['jane', 'mary',''ann', 'cate']
# for person in people:
# #   print(f'current-person: {person}')

#break from a loop
# people = ['mercy', 'cess', 'cate', 'john', 'partric', 'moses']
# for person in people:
#   if person == 'partric':
#     break
#   print(f'current-person: {person}')

##continue

# people = ['mercy', 'cess', 'cate', 'john', 'partric', 'moses']
# for person in people:
#   if person == 'partric':
#     continue
#   print(f'current-person: {person}')

##Range
# people = ['ann', 'col', 'cess']
# for i in range(len(people)):
#   print(people[i])

for i in range(0, 8):
  print(f'number: {i}')

  ### While Loops
  count = 0
  while count < 10:
    print(f'Count: {count}')
    count +=1