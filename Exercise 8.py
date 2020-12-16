# Exercise8: Rock Paper Scissors
import random
Options = ['Rock', 'Paper', 'Scissors']

while True:
    rng = random.randrange(0, 2)
    again = ''
    player = int(input('Choose: [0]rock, [1]paper or [2]scissors.\n'))
    player = Options[player]
    player2 = Options[rng]

    if player == 'Rock' and player2 == 'Scissors':
        print(player + ' vs ' + player2 + '\nyou win!')
        again = input('try again? (y/n)')
        if again == 'n':
            break
    elif player == 'Paper' and player2 == 'Rock':
        print(player + ' vs ' + player2 + '\nyou win!')
        again = input('try again? (y/n)')
        if again == 'n':
            break
    elif player == 'Scissors' and player2 == 'Paper':
        print(player + ' vs ' + player2 + '\nyou win!')
        again = input('try again? (y/n)')
        if again == 'n':
            break
    elif player == player2:
        print(player + ' vs ' + player2 + '\ntry again')
    else:
        print(player + ' vs ' + player2 + '\nLoser')
        again = input('try again? (y/n)')
        if again == 'n':
            break

