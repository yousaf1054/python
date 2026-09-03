students = {
    "Python": 80,
    "SQL": 65,
    "Django": 45,
    "HTML": 72,
    "CSS": 40
}
passed_sub = 0
failed_sub = 0

for key, value in students.items():
    if (value >= 50):
        passed_sub += 1
        print(f"{key} : {value} -> PASS")
    else:
        failed_sub+=1
        print(f"{key} : {value} -> FAIL")

print("number of passed subjects",passed_sub)
print("number of failed subjects",failed_sub)