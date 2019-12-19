#a dictionary is a collection of key-value pair

student = {'name': 'Sahil', 'age': 27, 'address': 'Toronto'}

#access elements in dictionary

print(student['name'])
print(student['age'])
print(student['address'])

#dictionay can not have duplicate keys

#add items in dictionary 

car = {} #creates an empty dictionary

car['make'] = 'Maserati'
car['model'] = 'Ghibli'
car['year'] = 2018
car['color'] = 'Black'

print(car)

car['year'] = 1997 #overwrites the previous value for the year

print(car)

#how do we iterate over a dictionary

for item in car:
    print(item)
    print(car[item]) #print the values





cars = [ {'make': 'BMW', 'model': 'M1', 'year': 2019, 'color': 'white'},
       {'make': 'Audi', 'model': 'q6', 'year': 2018, 'color': 'black'},
         {'make': 'Honda', 'model': 'civic', 'year': 2014, 'color': 'red'},
         {'make': 'Toyota', 'model': 'prius', 'year': 2017, 'color': 'yellow'},
         {'make': 'Maserati', 'model': 'ghibli', 'year': 2016, 'color': 'black'} ]
#processing a list of dictionaries
count = 0
for car in cars:
    #count how many toyotas are there

    if car['make'] == 'Toyota':
        count += 1

print(count)


#write frequency_counter(string) pre-homework
'''
frequency_counter('a testy line of text')
'a' : 1
' ' : 4
't' : 3
'e' : 2
's' : 1
't' :

'''

#how to get keys

print(car.values())   #use the values() method
#to get both keys and values, use the items method
print(car.items())


for key, value in car.items():
    print(key, value)
