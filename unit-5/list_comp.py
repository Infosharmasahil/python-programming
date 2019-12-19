#list compehension can be used to create a new list from
# an exisitng one

nums = [1,3,6,8,9,11,15,18]

#create a new list with only the even numbers

even_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

#using list comprehension

new_even_nums = [num for num in nums if num % 2 == 0 ]

print(new_even_nums)

#a list with the square of the even numbers

even_square = [val * val for val in nums if val % 2 == 0]

print(even_square)

#create a list of the titles with 't' in their names

titles = ['Lord of the rings', 'the time machine', 'The great getsby', 'Moby Dick', 'chronicles of narina']

t_list = [movie for movie in titles if 'T' or 't' in movie]

print(t_list)

#convert a string to uppercase
string = 'This is sample string'
#create a list of the characters-uppercase
capital = ' '.join([char.upper() for char in string])

print(capital)


#if/else goes before the for
#if number is < 10, add ten, else subtract ten

vals = [15,12,3,8,-1,7,11,25,0,10]

ten_list = [ val + 10 if val < 10 else val -10 for val in  vals ]

print(ten_list)

#dictionary comprehension

person = {'Name': 'Alice', 'Job': 'Engineer', 'City': 'Toronto'}

#create a new dictionary that has the first initial of both key and value



new_person = {key[0]: value[0] for key,value in person.items()}

print(new_person)