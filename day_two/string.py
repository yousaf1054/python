name = "yousaf"

# accessing the string

print(f"first letter is {name[0]}")
print(f"last letter is {name[-1]}")
print(f"3rd letter is {name[2]}")
print(f"length of the string {len(name)}")

# slicing the string
# [start:stop:jump]

print(f"first three charecter {name[0:3]}")
print(f"last three charecter {name[-3:len(name)]}")
print(f"name with out its first charecter {name[1:]}")
print(f"backword string {name[-1::-1]}")
print(f"backword string {name[-1:2:-2]}")

# string methode

str = "   Python Is Awesome   "
print(str.lower())
print(str.upper())
print(str.strip())
print(str.replace("Awesome", "powerful"))
print(str.strip().split(" "))
print(str.split())

# list and its operations

a1 = ["Django", "Python", "SQL", "React"]
print("printing the list ", a1)
print("first skill ", a1[0])
print("last skill ", a1[-1])
print("second ", a1[1])
print("number of skills in the list ", len(a1))

# list modification

a1[-1] = "TypeScript"
print("list after replace react by typescript", a1)
a1.append("FastAPI")
print("list after adding fastapi", a1)
a1.insert(1, "docker")
print("list after adding docker in the second possition", a1)
a1.remove("SQL")
print("list after remove the SQL", a1)

a1.pop(0)
print("list after pop()", a1)
a2 = [100, 0, 4, 232, 3333, 445, 1]
a2.sort()
print("list after sorting", a2)
a1.reverse()
print("list after the reverse", a1)
print("Python" in a1)
a2.clear()
print(a2)
a1.append("SQL")
a1.append("SQL")
a1.append("sql")
print(a1)
a1.remove("SQL")
print(a1)

# list slicing

print(a1[0:3])  # first three items
print(a1[-1:-3:-1])  # last two
print(a1[1:])  # items with ot first
print(a1[-1::-1])  # items reversed

# tuples

a3 = ("sunday", "monday", "tuesday", "wednesday",
      "thursday", "friday", "saturday")
print(a3)
print(a3[0])
print(a3[-1])
print(a3[0:3])
print(len(a3))
# a3[0]="hello"
print(a3)

tech_set = {"Django", "Python", "Django", "Python", "SQL", "React", "Python"}
print(tech_set)
print(len(tech_set))
tech_set.add("FastAPI")
print(tech_set)
tech_set.remove("SQL")
print("Python" in tech_set)

# set operations

Set_A = {"Python", "Django", "SQL"}
Set_B = {"Python", "React", "SQL"}
print(Set_A.union(Set_B))
print(Set_A.intersection(Set_B))
print(Set_A.difference(Set_B))
print(Set_B.difference(Set_A))

# dictionary

student = {"name": "yousaf", "age": 22,
           "city": "malappuram", "course": "python"}
print(student)
print(student["name"])
print(student["age"])
student["email"] = "hjfkvvkjb"
print(student)
student["course"] = "jjkdjf"
print(student)
student.pop("city")
print(student)
print(student.get("email"))

# Dictionary Methods

print(student.keys())
print(student.values())
print(student.items())
print(student.get("phone"))   # returns None if missing

print("name" in student)
print("phone" in student)
