# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
#IMPORT 
### core modules
import datetime
today = datetime.date.today()
from time import time
timestamp = time()
# # print(today)
# print(timestamp)

## Pip module
# from camelcase import CamelCase
# c = CamelCase()
# print(c.hump('Hello Teyce'))


##3 Import Custom Module
from validator import validate_email
email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')
