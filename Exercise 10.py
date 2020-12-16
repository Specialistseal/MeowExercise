# Exercise10: List Overlap Comprehensions
import random

a = [random.randrange(1, 26) for i in range(0, 10)]
b = [random.randrange(1, 26) for n in range(0, 13)]
overlap =[]
for num in a and b:
    if num in a and num in b and num not in overlap:
        overlap.append(num)
print(a)
print(b)
print(overlap)
