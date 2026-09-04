def calculate(num1, num2):
    total = num1 + num2
    difference = num1 - num2
    product = num1 * num2

    return total, difference, product


num1 = 20
num2 = 5

sum_result, difference_result, product_result = calculate(num1, num2)

print("Sum :", sum_result)
print("Difference :", difference_result)
print("Product :", product_result)

# default parameter


def greet(name="Guest"):
    print("Hello", name)


greet("yousaf")  # Output: Hello yousaf
greet()  # Output: Hello Guest


# scop of a variable
x = 10  # Global variable


def my_function():
    y = 5  # Local variable
    print("Inside the function, x =", x)  # Accessing global variable
    print("Inside the function, y =", y)  # Accessing local variable


my_function()  # Output: Inside the function, x = 10
#         Inside the function, y = 5

print("Outside the function, x =", x)  # Output: Outside the function, x = 10
# print("Outside the function, y =", y)  # This will raise an error because y is not defined outside the function


def age(age):
    if age >= 18:
        return "You are an adult"
    else:
        return "You are a minor"


age_input = int(input("Enter your age: "))
result = age(age_input)
print(result)

# function with loop


def print_numbers(list):
    sum = 0
    for num in list:
        sum += num
    return sum


list_of_numbers = [1, 2, 3, 4, 5]
total_sum = print_numbers(list_of_numbers)
print("Total sum:", total_sum)


# function with dictionaries
student_dbs = []


def management(student):
    student_dbs.append(student)
    for item in student_dbs:
        print(f"name : {item['name']}")
        print(f"age : {item['age']}")
        print(f"course : {item['course']}")


name = input("Enter your name : ")
age = int(input("Enter your age : "))
course = input("Enter your course name : ")
student = {"name": name, "age": age, "course": course}

management(student)


# *args → variable number of positional arguments
def test(*args):
    total = 0
    for i in args:
        total += i
    return total


result = test(10, 22, 56, 1)
print(sum_result)

# **kwargs → variable number of keyword arguments


def stdmanage(**std):
    for key,value in std.items():
        print(f"{key} : {value}")

stdmanage(name="yousaf",age=22,city="malappuram",mail="hsjjdj@gmail.com")


# lamda function

resultmul=lambda number: number*number
result = resultmul(5)
print(result)