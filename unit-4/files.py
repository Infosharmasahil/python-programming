#how to read a file
'''
my_file = open('lines.txt', 'r')

data = my_file.read()

my_file.close() #you should close a file after using it

print(data)

my_file = open('lines.txt', 'w') #overwrites the contents of the file, ifitexists
my_file.write('Please add this new line')
my_file.close()


my_file = open('new-file.txt', 'w')
my_file.write('lines for my new file')
my_file.close()

#we can use 'with' if we dont want to have to close everytime.
'''
with open('lines.txt') as my_file:

    data = my_file.read()
my_file = 'lines.txt'
print(data)