names = ["Yousaf", "Ali", "Ahmed", "John"]
marks = [85, 72, 91, 68]
result = zip(names, marks)
print(list(result))


names = ["Yousaf", "Ali", "Ahmed", "John"]

ages = [22, 21, 23]

courses = ["Python", "Java", "Django", "React"]
result = zip(names, ages, courses)
print(list(result))

names = ["Yousaf", "Ali", "Ahmed", "John"]
marks = [85, 72, 91, 68]
result = dict(zip(names, marks))
print(result)

names = ["Yousaf", "Ali", "Ahmed", "John", "Rahul"]
marks = [85, 45, 92, 68, 78]
result =(zip(names, marks))
result = filter(lambda x: x[1] >= 70, result)
result = dict(map(lambda x: (x[0], x[1]+5), result))
print(result)
