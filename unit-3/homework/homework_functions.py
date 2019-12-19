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



#functions for two arguments

def pivot_split(my_list, my_num):
    left = []
    right = []
    for num in my_list:
        if num < my_num:
            left.append(num)

        else:
            right.append(num)

    return [left, right]

print(pivot_split([12, 30, 22, 4, -6, 88], 9))




#isogram function

def is_isogram(phrase):
    
    letter_list = []

    for letter in phrase:
        
            if letter in letter_list:
                return False
            else:
                letter_list.append(letter)
    return True
    
print(is_isogram('abc'))
print(is_isogram('abcdea'))
