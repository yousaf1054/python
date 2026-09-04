data_base = []


def data_checking(data_base):
    if (len(data_base) == 0):
        print("in our system currently there is no student data first you want to add one student.")
        return False
    else:
        return True


def print_stdent_details(data_base):
    for student in data_base:
        print(f"ID : {student['std_id']}")
        print(f"Name : {student['name']}")
        print(f"Age : {student['age']}")
        print("\n")

# function for total_mark


def calculate_total_mark(data):
    return data['python_m']+data['sql_m']+data['django_m']+data['css_m']+data['html_m']

# function calculating percentage


def calculate_percentage(total_mark):
    return (total_mark/500)*100

# function for calculating grade


def calculate_grade(percentage):
    if (90 <= percentage):
        grade = "A+"
    elif (80 <= percentage <= 89):
        grade = "A"
    elif (70 <= percentage <= 79):
        grade = "B"
    elif (60 <= percentage <= 69):
        grade = "C"
    elif (50 <= percentage <= 59):
        grade = "D"
    else:
        grade = "F"
    return grade

# function for calculating result


def calculating_result(grade):
    if (grade == "F"):
        return "FAIL"
    else:
        return "PASS"


while (True):
    # meanu
    print("\n")
    print("========== STUDENT MANAGEMENT SYSTEM ==========\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Student Result")
    print("5. Show Class Statistics")
    print("6. Show Available Courses")
    print("7. Exit\n\n")
    choice = int(input("enter you choice : "))

    # add student
    if (choice == 1):
        # detail query
        print("Enter your deatils :: \n")
        name = input("Enter your name : ")
        std_id = input("Enter the student id number : ")
        age = int(input("Enter your age : "))
        course = input("Enter the course name : ")
        python_m = int(input("Enter the mark of the python : "))
        sql_m = int(input("Enter thr mark of the SQL : "))
        django_m = int(input("Enter the mark of the Django : "))
        html_m = int(input("Enter the mark of the HTML : "))
        css_m = int(input("Enter the mark of the CSS : "))

        student = {"name": name, "std_id": std_id, "age": age, "course": course, "python_m": python_m,
                   "sql_m": sql_m, "django_m": django_m, "html_m": html_m, "css_m": css_m}
        data_base.append(student)
        print("\nstudent added successfully. ")

    elif (choice == 2):
        check = data_checking(data_base)
        if (check == False):
            continue
        else:
            print("\n================Details of entered students=============\n")
            print_stdent_details(data_base)
    elif (choice == 3):
        check = data_checking(data_base)
        if (check == False):
            continue
        else:
            flag = 0
            search_id = input("\nenter the student id : ")
            for student in data_base:
                if (student["std_id"] == search_id):
                    print("Student found")
                    print(f"Name :{student['name']}")
                    print(f"Age :{student['age']}")
                    print(f"Course :{student['course']}")
                    flag = 1
                    break
            if (flag == 0):
                print("\nstudent not in the registred list so enter first. \n")

    elif (choice == 4):
        check = data_checking(data_base)
        if (check == False):
            continue
        else:
            flag = 0
            result_id = input("\nenter the student id : ")
            for student in data_base:

                if (student["std_id"] == result_id):

                    print("Result found\n")

                    print(f"Name :{student['name']}")
                    print(f"Course :{student['course']}")
                    print(f"python :{student['python_m']}")
                    print(f"sql :{student['sql_m']}")
                    print(f"css :{student['css_m']}")
                    print(f"html :{student['html_m']}")
                    print(f"Django :{student['django_m']}")

                    total_mark = calculate_total_mark(student)

                    print("\nToatal mark of the student is : ", total_mark)

                    percentage = calculate_percentage(total_mark)
                    print("\npercentage is : ", percentage)
                    grade = calculate_grade(percentage)

                    print(f"Grade : {grade}")
                    status = calculating_result(grade)
                    print(f"status : {status}")
                    flag = 1
                    break
            if (flag == 0):
                print("\nstudent not in the registred list so enter first. \n")

    elif (choice == 5):
        check = data_checking(data_base)
        if (check == False):
            continue
        else:
            print("\n================Class Statistics=============\n")
            total_students = len(data_base)
            passed_students = 0
            failed_students = 0
            total_percentage = 0
            highest_percentage = 0
            lowest_percentage = 100

            for student in data_base:
                total_mark = calculate_total_mark(student)

                percentage = calculate_percentage(total_mark)
                total_percentage += percentage

                if percentage > highest_percentage:
                    highest_percentage = percentage

                if percentage < lowest_percentage:
                    lowest_percentage = percentage

                grade = calculate_grade(percentage)
                result_pass_or_fail = calculating_result(grade)
                if (result_pass_or_fail == "PASS"):
                    passed_students += 1
                else:
                    failed_students += 1

            class_average = total_percentage / total_students

            print(f"Total number of students : {total_students}")
            print(f"Number of passed students : {passed_students}")
            print(f"Number of failed students : {failed_students}")
            print(f"Class average percentage : {class_average}")
            print(f"Highest percentage : {highest_percentage}")
            print(f"Lowest percentage : {lowest_percentage}")

    elif (choice == 6):
        check = data_checking(data_base)
        if (check == False):
            continue
        else:
            print("\n================Available Courses=============\n")
            courses = set()
            for student in data_base:
                courses.add(student['course'])
            print("Available Courses:")
            for course in courses:
                print(course)

    elif (choice == 7):
        print("\nExiting the program. Goodbye!")
        break
