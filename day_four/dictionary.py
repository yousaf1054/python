numbers = [10, 20, 30, 40, 50]
result = {number: number*number for number in numbers}
print(result)

numbers = [10, 15, 22, 31, 40, 53, 60]
result = {number: number*2 for number in numbers if number % 2 == 0}
print(result)

students = {
    "Yousaf": 85,
    "Ali": 45,
    "Ahmed": 92,
    "John": 68,
    "Rahul": 78
}


result = {key: value+5 for key, value in students.items() if value >= 50}
print(result)

result = {key: "D" if 50 <= value <= 59 else "C" if 60 <= value <= 69 else "B" if 70 <= value <= 79 else "A" if 80 < value <= 89 else "A+" for key, value in students.items() if value >= 50}
print(result)
