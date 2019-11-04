import random



name = input('Enter your name: ')
random_message = ['You are awesome', 'you are a party animal', 'you are crazy', 'you need to focus', 'time to sleep', 'you are a winner', 'are you hungry']

while name != 'e':
    print(name +'!', random.choice(random_message))
    name = input('Enter your name: ')

    if name == 'e':
        print('End of Game')
  




