#the for loop
'''
name = 'sahil'
for count in range(1, 11):
    print(name)


#print the odd numbers between 1 and 10

for num in range(1, 11):
    if num % 2 == 1:
        print(num)

#print the sum of the even numbers

total = 0

for num in range(1, 11):
    if num % 2 == 0:
       total = num + total
print(total)

total += num


#store your full name in a variable
#loop over your name
#if you find a vowel, print it
#'a', 'e', 'i', 'o', 'u' - vowels

full_name = 'Sahil Sharma'

for char in full_name:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(char)


small_number = 0
my_numbers = [3, 5, 17, 11, 21, 53, -10, -27, 45, 80]

for n in my_numbers:
    if n < small_number:
        small_number = n

print(small_number)


my_numbers = [3, 5, 17, 11, 21, 53, -10, -27, 45, 80]

print(min(my_numbers))

weights = [[50, 25, 75], [95.7, 38.3, 55.2], [88, 45, 16]]
averages = []
for item in weights:
    list_total = 0
    for value in item:
        list_total += value
    averages.append(list_total/len(item))


print(averages) 

*
**
***
****
*****
******
*******
********
*********



for row in range(1, 11):
    for col in range(1, row + 1):
        print('*', end=' ')
    print()



#using indexes to access list items
#use index if we need to edit items in list

#set all the negative readings to 0

readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

for idx in range(len(readings)):
    if readings[idx] < 0:
        readings[idx] = 0

print(readings)


#find the position of an item in a list
'''
current_age = 25
ages = [15, 17, 35, 12, 25, 55, 40, 31, 20]
    
for idx in range(len(ages)):
    if ages[idx] == current_age:
        print('current_age is found at position', idx)





