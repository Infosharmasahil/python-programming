import random

player_one_total = 0
player_two_total = 0

turn = 1

max_score = 20

while True:
    choice = input('Player {}Roll or Hold [r/h]'.format(turn))
    val = random.randint(1, 6)
    if choice == 'r':
        print('Player {} rolls {}'.format(turn, val))
        if val != 1:
            if turn == 1:
               player_one_total += val
            else:
                player_two_total += val

        else:
            print('Player {} loses turn'.format(turn))
            if turn ==1:
               player_one_total = 0
               turn = 2 
            else:
                player_two_total = 0
                turn = 1

    else:
        print('Player {} holds'.format(turn))
        if turn == 1:
            turn = 2
        else:
            turn = 1

    #check if someone wins the game
    if player_one_total >= max_score or player_two_total >= max_score:
        break

if player_one_total >= max_score:
    print('Player 1 wins !!!')
else:
    print('print 2 wins !!!')



