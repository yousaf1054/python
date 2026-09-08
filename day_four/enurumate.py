names = ["Yousaf", "Ali", "Ahmed", "John", "Rahul"]
for index,name in enumerate(names):
    print(f"Index: {index}, Name: {name}")

courses = ["Python", "SQL", "Django", "HTML", "CSS"]
for index,course in enumerate(courses,start=1):
    print(f"{index}. {course}")

marks = [85, 45, 92, 68, 78]
for index,mark in enumerate(marks,start=1):
    if mark >= 70:
        print(f"{index}. {mark}")


names = ["Yousaf", "Ali", "Ahmed", "John", "Rahul"]
marks = [85, 45, 92, 68, 78]
result=zip(names,marks)
for index,x in enumerate(result,start=1):
    if x[1] >= 70:
        if x[1] >= 90:
            print(f"{index}. {x[0]} - {x[1]} - A+")
        elif x[1] >= 80:
            print(f"{index}. {x[0]} - {x[1]} - A")
        elif x[1] >= 70:
            print(f"{index}. {x[0]} - {x[1]} - B")