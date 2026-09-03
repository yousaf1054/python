data_base = []

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
        print("\n================Details of entered students=============\n")
        for student in data_base:
            print(f"ID : {student['std_id']}")
            print(f"Name : {student['name']}")
            print(f"Age : {student['age']}")
            print("\n")
    elif (choice == 3):
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

                total_mark = student['python_m']+student['sql_m'] + \
                    student['django_m']+student['html_m']+student['css_m']

                print("\nToatal mark of the student is : ", total_mark)

                percentage = (total_mark/500)*100
                print("\npercentage is : ", percentage)
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

                print(f"Grade : {grade}")
                if (grade == "F"):
                    print("Status : FAIL")
                else:
                    print("Status : PASS")
                flag = 1
                break
        if (flag == 0):
            print("\nstudent not in the registred list so enter first. \n")

    elif (choice == 5):
        print("\n================Class Statistics=============\n")
        # Total students
        # Number of passed students
        # Number of failed students
        # Class average percentage
        # Highest percentage
        # Lowest percentage
        total_students = len(data_base)
        passed_students = 0
        failed_students = 0
        total_percentage = 0
        highest_percentage = 0
        lowest_percentage = 100

        for student in data_base:
            total_mark = student['python_m']+student['sql_m'] + \
                student['django_m']+student['html_m']+student['css_m']

            percentage = (total_mark/500)*100
            total_percentage += percentage

            if percentage > highest_percentage:
                highest_percentage = percentage

            if percentage < lowest_percentage:
                lowest_percentage = percentage

        class_average = total_percentage / total_students*100

        print(f"Total number of students : {total_students}")
        print(f"Number of passed students : {passed_students}")
        print(f"Number of failed students : {failed_students}")
        print(f"Class average percentage : {class_average}")
        print(f"Highest percentage : {highest_percentage}")
        print(f"Lowest percentage : {lowest_percentage}")

    elif (choice == 6):
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
