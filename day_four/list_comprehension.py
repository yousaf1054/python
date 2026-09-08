numbers1 = [10, 15, 22, 31, 40, 53, 60]

even_numbers = []

even_numbers = [number
                for number in numbers1 if number % 2 == 0]


print(even_numbers)


numbers = [2, 5, 8, 11, 14, 17, 20]
squer = [number*number for number in numbers if number % 2 == 0]
print(squer)

names = ["yousaf", "ali", "ahmed", "john", "mohammed"]
result = [name for name in names if len(name) > 4]
print(result)


numbers = [10, 15, 22, 31, 40, 53]
order = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(order)

numbers = [1, 2, 3, 4, 5]
result = [number*2 for number in numbers if number > 2]
print(result)

# nested
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

result = [x+y for x in numbers1 for y in numbers2]
print(result)

numbers = [1, 2, 3, 4, 5]
result = [x*y for x in numbers for y in numbers]
print(result)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [number1 for number in numbers for number1 in number if number1 % 2 == 0]
print(result)

result = [
    number1*number1 for number in numbers for number1 in number if number1 % 2 == 0]
print(result)

numbers = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]
result = [number1 for number in numbers for number1 in number if number1 %
          2 == 0 and number1 > 20]
print(result)

students = [
    ["Yousaf", "Ali"],
    ["Ahmed", "John"],
    ["Rahul", "David"]
]
result = [
    student for group in students for student in group if len(student) > 4]
print(result)


# advanced

students = [
    {"name": "Yousaf", "marks": [80, 90, 75]},
    {"name": "Ali", "marks": [60, 45, 70]},
    {"name": "Ahmed", "marks": [95, 85, 90]}
]
result = [mark for student in students for mark in student["marks"] if mark >= 80]
print(result)
