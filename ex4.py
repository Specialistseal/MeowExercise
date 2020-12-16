# Exercise4: Divisors

num = int(input('pick a number: '))
divi_list = list(range(1, (num + 1)))
for x in divi_list:
    if num % x == 0:
        print(str(x) + ' is a divisor of ' + str(num))
