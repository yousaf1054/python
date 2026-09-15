try:
    age = int(input("Enter your age : "))
    if age < 0:
        raise ValueError("age cant be negative")
    elif age > 120:
        raise ValueError("enter the possibel number of age")
    else:
        print(age)
except ValueError as e:
    print(e)


class InvalidMarkError(Exception):
    pass


try:
    mark = int(input("Enter mark: "))

    if mark < 0 or mark > 100:
        raise InvalidMarkError("Mark must be between 0 and 100")

    print("Valid mark:", mark)

except InvalidMarkError as e:
    print(e)

except ValueError:
    print("Please enter a number.")
