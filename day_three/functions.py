def add(num1, num2):
    return num1 + num2


def greet(name):
    print("hello ", name)

def dtails(name,age,course):
    print(f"name : {name}\nage : {age}\ncourse : {course}")
name = input("enter your name : ")
age = int(input("enter the age : "))
course = input("enter the course name : ")
# positional argument
dtails(name,age,course)
# keyword argument
dtails(age=age,name=name,course=course)
num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
result = add(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")




def test():
    x = 10

test()
print(x)