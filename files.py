# Python has functions for creating, reading, updating, and deleting files.
# How to create a File
##Open a file
teyce = open('teyce.txt', 'w')

##Get some info into the file
print('name ', teyce.name)
print('Is closed ', teyce.closed)
print('Opening mode ', teyce.mode)

###write to file
teyce.write(' I am learning python ')
teyce.write(' So that I can do Backend End Development.')
teyce.write('I have just completed Front End Development, ')

#append
teyce = open('teyce.txt', 'a')
teyce.write('and I am hoping python is as interesting as HTML and CSS. ')
# teyce.close()

#Read from a file
teyce = open('teyce.txt', 'r+')
text = teyce.read(150)
print(text)
