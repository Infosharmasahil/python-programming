#function for reverse_list

def reverse(lists):
    lists.reverse()
    return lists

lists = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(reverse(lists))


 #Reversing a list using slicing technique

def reverse(new_lists):
    new_lists = lists[::-1]
    return new_lists

lists = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(reverse(lists))




from string import ascii_lowercase

letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}

def alphabet_position(text):
    text = text.lower()
    numbers = [letters[character] for character in text if character in letters]
    return ''.join(numbers)

print(alphabet_position('abc'))

print(alphabet_position('Happy'))

'''

#functions for two arguments


def search(pivot_split, pivot):
    number = ''
    for number in pivot:
        if number <= pivot:
            return pivot_split + pivot
        else:
            return pivot_split + pivot
        
pivot_split = [10, 20, 30, 40, 50, 60, 70, 80, 90]
pivot = [62]

print(number)

'''
#isogram function

def is_isogram(phrase):
    
    letter_list = []

    for letter in phrase:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)
    return True
    
print(is_isogram('abc'))
print(is_isogram('abcdea'))
