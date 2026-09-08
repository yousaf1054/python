numbers = [10, 15, 22, 31, 40, 53, 60]
result=filter(lambda x:x%2==0 and x>20,numbers)
print(list(result))

names = ["Yousaf", "Ali", "Ahmed", "John", "Mohammed", "Rahul"]
result=filter(lambda x:len(x)>4,names)
print(list(result))

def is_greater(number):
    return number > 30
numbers = [12, 17, 24, 31, 40, 55, 68]
result = filter(is_greater, numbers)
print(list(result))


students = {
    "Yousaf": 85,
    "Ali": 45,
    "Ahmed": 92,
    "John": 68,
    "Rahul": 78
}
result = filter(lambda item: students[item[0]] >= 70, students.items())
print(list(result))