# Exercise 14: List Remove Duplicates
import random


def un_duplicate_inator(given_list):
    """this functaions will take out all the duplicates from lists"""
    return list(set(given_list))


a = [random.randrange(1, 11) for i in range(1, 10)]
print('the list is: ', a)
b = un_duplicate_inator(a)
print('now with no duplicates the list looks like this: ', b)