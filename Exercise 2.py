# Exercise2: Odd or Even

num = int(input('pick a number: '))
if num % 4 == 0:
    print("The number is dividable by 4")
elif num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
    print("")

# Exercise2: Odd or Even, Extra2

num = int(input('pick a number: '))
check = int(input('pick a divider: '))
if num % check == 0:
    print("The numbers divide Evenly")
else:
    print('The numbers divide Oddly')  # yes i know thats a typo but it made me chuckle... Meow
