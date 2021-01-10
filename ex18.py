# Exercise 18: Cows And Bulls
# cow = correct number in correct place
# bull correct number in the wrong place
#import random
#import string


"""def rand_num():
    # This is fanction generates a random 4 digit number
    return ''.join(random.choice(string.digits) for _ in range(0, 4))"""


def digit_check(guess, goal):
    if x in range(0,3)

    return cow, bull


#goal = rand_num()
goal = [1, 2, 3, 4]
count = 0
print("I will generate a random 4 digit number and you will have to guess what the number is")
print("""for ever correct number in the wrong space you will earn a "bull"
and for every correct number in the right place you will get a "cow" \nwhat is your guess? \n""")


while True:
    guess = [input()]

    if guess != goal:
        count += 1
        cow, bull = digit_check(guess, goal)
        print("Cows: " + str(cow) + "Bulls: " + str(bull))

    if guess == goal:
        print("you won\nit took you " + str(count) + "tries")
        break