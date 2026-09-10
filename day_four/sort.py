numbers = [45, 12, 89, 23, 67, 10, 34]
result = sorted(numbers)
print(result)

result = sorted(numbers, reverse=True)
print(result)


names = ["Yousaf", "Ali", "Ahmed", "John", "Mohammed", "Rahul"]
result = sorted(names,key=lambda x: len(x), reverse=True)
print(result)
names = ["Yousaf", "Ali", "Ahmed", "John", "Mohammed", "Rahul"]
result = sorted(names,key=lambda x: len(x))
print(result)

students = [
    {"name": "Yousaf", "marks": 85},
    {"name": "Ali", "marks": 45},
    {"name": "Ahmed", "marks": 92},
    {"name": "John", "marks": 68},
    {"name": "Rahul", "marks": 78}
]
result = sorted(students, key=lambda x: x["marks"] ,reverse=True)
print(result)

marks = [85, 45, 92, 68, 78, 55, 90]

result=min(marks)
print(result)
result=max(marks)
print(result)
sum_marks = sum(marks)
print(sum_marks)
avarage_marks = sum_marks / len(marks)
print(avarage_marks)


marks = [85, 45, 92, 68, 78]
result = any(mark < 50 for mark in marks)
print(result)

result = all(mark > 40 for mark in marks)
print(result)

result = all(mark >= 50 for mark in marks)
print(result)


result = all(mark > 40 for mark in marks) and any(mark >=90 for mark in marks)
print(result)