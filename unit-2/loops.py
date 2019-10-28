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
'''

#store your full name in a variable
#loop over your name
#if you find a vowel, print it
#'a', 'e', 'i', 'o', 'u' - vowels

full_name = 'Sahil Sharma'

for char in full_name:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(char)







