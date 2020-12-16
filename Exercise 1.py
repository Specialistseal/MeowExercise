# Exercise1: Character Input

name = input('What is your name: ')
age = input('How old are you: ')
y100 = 100 - int(age)
message = name + ' you will be 100 years old at the year ' + str(2020 + y100)
print(message)
copies = int(input('how many copies would you like? '))
while copies != 0:
    print(message)
    copies -= 1
