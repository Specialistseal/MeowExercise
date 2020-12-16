# Exercise5: List Overlap
import random

a = [random.randrange(0, 51, 1) for i in range(0, 20, 1)]
b = [random.randrange(0, 51, 1) for j in range(0, 20, 1)]
overlap = []
for num in a:
    if num in b and num not in overlap:
        overlap.append(num)
print(overlap)
