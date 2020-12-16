#Exercise3: List Less Than Ten

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for num in my_list:
    if num <= 5:
        new_list.append(num)
print(new_list)
