with open("student.txt", "r") as file:
    content = file.read()

print(content)
print(type(content))

# readline()
with open("student.txt", "r") as file:
    readline_1 = file.readline()
    readline_2 = file.readline()

print(readline_1)
print(readline_2)

# readlines() this methode give entire file as list

with open("student.txt", "r") as file:
    content = file.readlines()

print(content)

with open("new_students.txt", "w") as file:
    file.write("Yousaf,85\n")
    file.write("Ali,72\n")
    file.write("Ahmed,91\n")
    file.write("hello,91\n")
# append content
with open("new_students.txt", "a") as file:
    file.write("Yousaf,85\n")
    file.write("Ali,72\n")
    file.write("Ahmed,91\n")
    file.write("hello,91\n")

# file creation
#with open("new_students_test.txt", "x") as file:
 #   file.write("Yousaf,85\n")
  #  file.write("Ali,72\n")
   # file.write("Ahmed,91\n")
    #file.write("hello,91\n")


students = [
    "Yousaf,85\n",
    "Ali,72\n",
    "Ahmed,91\n",
    "John,70\n"
]
with open("students2.txt", "x") as file:
    file.writelines(students)