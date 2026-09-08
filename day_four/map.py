# map()
numbers = [2, 5, 8, 10, 15]
result = map(lambda x: x**2, numbers)
print(list(result))


def double(number):
    return number*2


result = map(double, numbers)
print(list(result))


def add(num1, num2):
    return num1+num2


numbers1 = [10, 20, 30, 40]
numbers2 = [1, 2, 3, 4]
result = map(add, numbers1, numbers2)
print(list(result))




numbers = [10, 15, 22, 31, 40, 53, 60]
result = map(lambda x:"Even" if x%2==0 else "Odd",numbers)
print(list(result))
def double(number):
    return number*2

numbers = [10, 15, 22, 31, 40, 53, 60]
result = map(double, numbers)
print(list(result))