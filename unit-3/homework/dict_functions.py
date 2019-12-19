
frequency_counter = ('happy')
# using dict.get() to get count of each element in string
freq = {} 
  
for keys in frequency_counter:
    freq[keys] = freq.get(keys, 0) + 1

print(str(freq))



def frequency_counter(string):
    result = {}
    for character in string:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1

    return result

print(frequency_counter('happy'))

#dict = {'name': 'sahil', 'age': '27years', 'location' : 'Toronto'}

#print(dict['location'])


def convert(list_to_dict, val):
    val = dict(list_to_dict)
    return val

list_to_dict = ([['name', 'Alice'], ['job', 'Engineer'],['city', 'Toronto']])

dictionary = {}
print(convert(list_to_dict, dictionary))


def list_to_dict(people):
    result = {}
    for item in people:
        result[item[0]] = item[1]

    return result

person = ([['name', 'Alice'], ['job', 'Engineer'],['city', 'Toronto']])

print(list_to_dict(person))


