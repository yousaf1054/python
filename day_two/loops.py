# loops

skills = ["Python", "Django", "SQL", "React", "FastAPI"]

for i in skills:
    print(i)

for i in range(1, 11):
    print(i)

print("steps in the loop")
for i in range(1, 11, 3):
    print(i)

# control statement "if ,elif, else"

age = int(input("enter your age : "))
if (age < 13):
    print("you are a child")
elif (13 <= age <= 17):
    print("you are a teenager")
elif (18 <= age <= 59):
    print("you are an adult")
else:
    print("your are a senior")

# admission eligbility
age = int(input("enter your age : "))
per = int(input("enter your mark percentage : "))
id_card = True

if (18 <= age and 60 <= per and id_card):
    print("you are eligible")
else:
    print("not eligible")


numbers = [10, 15, 22, 31, 40, 53, 60]
for number in numbers:
    if (number % 2 == 0):
        print(number)

# while loop

count = 1
while (count <= 5):
    print(count)
    count += 1

# break
count = 1
while (count):
    if (count > 5):
        break
    print(count)
    count += 1
print("condinue")
# countinue
count = 1
while (count <= 10):
    if (count == 5):
        count += 1
        continue
    print(count)
    count += 1


# nested loops

for i in range(1, 4):
    for j in range(1, 4):
        print(i,j)
    print("\n")
