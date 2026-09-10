from functools import reduce    
def calculate_grade(average_mark):
    if (90 <= average_mark <= 100):
        grade = "A+"
        return grade
    elif (80 <= average_mark <= 89):
        grade = "A"
        return grade
    elif (70 <= average_mark <= 79):
        grade = "B"
        return grade
    elif (60 <= average_mark <= 69):
        grade = "C"
        return grade
    elif (50 <= average_mark <= 59):
        grade = "D"
        return grade
    else:
        grade = "F"
        return grade


def pass_or_fail(av_mark, marks):
    if av_mark >= 50 and all(mark >= 40 for mark in marks):
        return "PASS"
    else:
        return "FAIL"


def distinction(av_mark, marks):
    if (av_mark >= 85 and any(mark >= 95 for mark in marks)):
        return "YES"
    else:
        return "NO"


students = [
    {"name": "Yousaf", "marks": [85, 92, 78, 88, 95]},
    {"name": "Ali", "marks": [45, 52, 48, 60, 55]},
    {"name": "Ahmed", "marks": [95, 89, 92, 96, 91]},
    {"name": "John", "marks": [68, 72, 65, 70, 75]},
    {"name": "Rahul", "marks": [78, 82, 80, 85, 79]},
    {"name": "David", "marks": [35, 42, 38, 45, 40]},
    {"name": "Mohammed", "marks": [88, 91, 84, 90, 87]}
]
total_students = len(students)
subjects = ["Python", "SQL", "Django", "HTML", "CSS"]
total_subject = len(subjects)
results = {}
for student in students:
    # individual mark analysis
    total_mark = sum(student['marks'])

    max_mark = max(student['marks'])

    min_mark = min(student["marks"])

    average_mark = total_mark/total_subject

    # grade calculation based on their average mark

    grade = calculate_grade(average_mark)

    status = pass_or_fail(average_mark, student["marks"])
    distinction_status = distinction(average_mark, student["marks"])

    # store the detais in a dictnory

    results[student["name"]] = {
        "total": total_mark,
        "average": average_mark,
        "highest": max_mark,
        "lowest": min_mark,
        "grade": grade,
        "status": status,
        "distinction": distinction_status
    }


ranking = sorted(results.items(), key=lambda x: x[1]['average'], reverse=True)
print("===== RANKING OF STUDENTS =====")
for index, student in enumerate(ranking, start=1):
    print(f"{index}. {student[0]}")

print("===== QUALIFYING STUDENTS =====")
qualified = list(filter(
    lambda x: x[1]['status'] == 'PASS' and x[1]['average'] >= 70, results.items()))

for student in qualified:
    print(student[0])

print("===== BONUS AVERAGE =====")
bonus = list(map(lambda x: (x[0], x[1]['average']+5), qualified))

for student in bonus:
    print(f"{student[0]} - {student[1]}")

print("===== CLASS STATISTICS =====")
average_mark_list = list(map(lambda x: x[1]['average'], results.items()))
class_av_ma = sum(average_mark_list)/total_students
print(f"Class avaerage malrk is : {class_av_ma}")
hiehyst_mark_ava = max(average_mark_list)
print(f"Highest Average mark is : {hiehyst_mark_ava}")
minst_mark_ava = min(average_mark_list)
print(f"Lowest Average mark is : {minst_mark_ava}")


flag1 = any(key[1]['grade'] == "A+" for key in results.items())
print("Any A+ Student: ", flag1)
flag2 = all(key[1]['status'] == "PASS" for key in results.items())
print("iS ALL STUDENT IS PASS : ", flag2)
subject_marks = {}

for student in students:
    for subject, mark in zip(subjects, student["marks"]):

        if subject not in subject_marks:
            subject_marks[subject] = []

        subject_marks[subject].append(mark)

print(subject_marks)

for subject, marks in subject_marks.items():

    total = reduce(lambda a, b: a + b, marks)

    print(f"{subject} - Total: {total}")
