# list comprehension = a concise way to create lists in python
# compact and easier to read 
# [expression for value in iterable if condition]


doubles = [x * 2 for x in range(1,11)]

numbers = [1, 2, -5, -4, 8, 3]
positive_num = [num for num in numbers if num > 0]

print(positive_num)