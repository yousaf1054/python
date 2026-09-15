try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Please enter a valid number.")


numbers = [10, 20, 30]
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
else:
    print("You entered:", number)


# filnally
try:
    x = int(input("enter a number that number divides 100 : "))
    result = 100/x
except ValueError:
    print("enter valid number")
except ZeroDivisionError:
    print("it is a logical error zero cant divide")
else:
    print(f'result is {result}')
finally:
    print("programm fully executed")


try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x/y)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
