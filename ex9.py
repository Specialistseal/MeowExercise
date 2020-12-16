# Exercise9: Guessing Game One
import random
rng = random.randrange(1, 10)
print('i have picked anumber from one to ten')
count = 0
guess = 0

while guess != rng and guess != 'exit':
    guess = input('would you like to guess what it is? \n')
    if guess == 'exit':
        print("you are not fun")
        break

    guess = int(guess)
    count += 1
    if guess < rng:
        print('too low')
    elif guess > rng:
        print('too high')
    else:
        print('big winner')
        print("it took you ", count, "tries")
