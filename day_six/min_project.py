def displayAllStudents():
    with open("students.txt", "r") as file:
        for line in file:
            content = line.strip()
            # print(content)
            name, mark = content.split(",")
            print(f"{name} -> {mark}")


def addStudent():
    name = input("Enter name: ")
    mark = int(input("Enter mark: "))

    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100")

    with open("students.txt", "a") as file:
        file.write(f"{name},{mark}\n")


def searchStudent(name):
    with open("students.txt", "r") as file:
        for line in file:
            content = line.strip()
            name1, mark = content.split(",")
            if name == name1:
                print(f'{name} -> {mark}')
                return
        print("there is no student in data base named as ", name)


while True:

    try:
        print("===== menu =====\n")
        print("1. Add student.\n")
        print("2. Display all student detailes.\n")
        print("3. Search student.\n")
        print("4. Exit\n")
        option = int(input("Enter your option : "))
        if (option == 1):
            addStudent()
        elif (option == 2):
            displayAllStudents()
        elif (option == 3):
            name = input("Enter student name : ")
            searchStudent(name)
        elif option == 4:
            print("goodbay")
            break
        else:
            print("enter valid option from the menu")
    except ValueError:
        print("Enter a valid mark between 0 and 100.")

    except FileNotFoundError:
        print("The file does not exist.")
