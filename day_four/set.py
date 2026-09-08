numbers = [10, 15, 10, 20, 15, 25, 30, 20]
result = {number*number for number in numbers}
print(result)

numbers = [10, 15, 22, 31, 40, 53, 60, 22, 40]
result = {number*2 for number in numbers if number % 2 == 0}
print(result)

names = ["Yousaf", "Ali", "Ahmed", "John", "Yousaf", "Ahmed", "Rahul"]
result = {name.upper() for name in names if len(name) > 4}
print(result)

students = {
    "Yousaf": [80, 90, 75],
    "Ali": [60, 45, 70],
    "Ahmed": [95, 85, 90],
    "John": [55, 65, 72]
}

result = {mark for name, marks in students.items()
          for mark in marks if mark >= 80}
print(result)

result = {mark**2 for name, marks in students.items()
          for mark in marks if mark >= 70}
print(result)

