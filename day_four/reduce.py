from functools import reduce
numbers = [2, 4, 6, 8, 10]
result = reduce(lambda x, y: x*y, numbers)
print(result)

numbers = [45, 12, 89, 23, 67, 91, 34]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)

result = reduce(lambda x, y: x if x < y else y, numbers)
print(result)

marks = [85, 45, 92, 68, 78]
result = reduce(lambda x, y: x+y, marks)
print(result)

numbers = [10, 15, 22, 31, 40, 53, 60]
result = list(filter(lambda x:  x % 2 == 0, numbers))
print(result)
result = reduce(lambda x, y: x+y, result)
print(result)
