# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#create a class

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email =email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age += 1


## Extend class
class Customer(User):
 def __init__(self, name, email, age):
        self.name = name
        self.email =email
        self.age = age
        self.balance = 0
 def set_balace(self, balance):
        self.balance = balance
 def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
 
  ##initiaiize user object(init)
teyce = User('Teyce Bobo','tee@gmail.com', 30 )
## init customer object
janet = Customer('janet mbugua', 'janee@gmail.com', 35)
janet.set_balace(500)
print(janet.greeting())
print(type(teyce))
print(teyce.name)
print(teyce.age)
teyce.has_birthday()
print(teyce.greeting())


