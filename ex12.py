# Exerices 12: List Ends
import random


def ends_append(given_list):
    # This list will take the first and last values from a list and put it in a new list.
    return [given_list[0], given_list[len(given_list)-1]]


a = [random.randrange(0, 26) for i in range(1, 11)]
print('first list: ', a)
new_list = ends_append(a)
print('new list: ', new_list)
