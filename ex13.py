# Exercise 13: Fibonacci

def fibonacci_generator(lengeth):
    """ this function generates Fibonacci numbers"""
    num1, num2 = 0, 1
    result = []
    for i in range(0, lengeth):
        num1, num2 = num2, num1 + num2
        result.append(num1)
    return result


number = int(input('how many Fibonacci numbers to generate?\n'))
answer = fibonacci_generator(number)
print(answer)