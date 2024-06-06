# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
#create a function
def Hello(name='Teyce'):
    print(f'Hello {name}')
# Hello()

#Return values
def sum(numx, numy):
    total= numx + numy
    return total
# print(sum(3, 4))

#Lamba
sum = lambda numx, numy: numx + numy
print(sum(10, 5))