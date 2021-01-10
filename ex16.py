# Exercise 16: Password Generator
import random
import string


def low_strength():
    return ''.join(random.choice(string.digits) for _ in range(0, 8))


def mid_strength():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(0, 8))


def high_strength():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(0, 8))


password = input("how strong would you like your password?\n options: (weak) [mid] {high}\n")
if password == "weak":
    print(low_strength())

elif password == "mid":
    print(mid_strength())

elif password == "high":
    print(high_strength())

else:
    print("what?")
