age = int(input("enter your age :"))
id = True
is_stdent = True

result = (age >= 18 and id) or (is_stdent and id)
print(result)


# age calculater
print("next is age calculator")
age = int(input("enter you age : "))
print(f"your age after 5 years is : {age+5}")

# simple billing

item_price = float(input("enter the price of the item : "))
qty = int(input("enter the qty of the item : "))
print(f"the total amount you have to pay : { qty * item_price }")


print("temparature transulater celsios to farenheat")
Celsius=float(input("enter temp in Celsius : "))
Fahrenheit = (Celsius * 9 / 5) + 32
print(f"the temp in Fahrenheit is : {Fahrenheit}")

