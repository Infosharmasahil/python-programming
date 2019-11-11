#function to add two integers



#function to display hello there

def say_hello():
    print('Hello World')

#function that returns the length of a string

def length(string):
    return len(string)


#function to return the sum of integers in a list

def sum_of_intergers(a_list):
    result = 0
    for num in a_list:
        if type(num) is int:
            result += num
            
    return result

#function to reverse a string



 
def reverse(s): 

    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 


def rev_string(string):
    idx = len(string) - 1
    result = ''
    while idx >= 0:
        result += string[idx]
        idx -=1

    return result

def reverse(str):
    str = ''

    for i in s:
        s = len(i[-1:0])
        return str

#reverse string in one line (python)

def one_line_reverse(string):
    return string[::-1]

