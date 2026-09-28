class InvalidMarkError(Exception):
    pass


def addStudent():
    try:

        name = input("Enter student name : ")
        mark = int(input("Enter student mark : "))
        if 0 > mark or mark > 100:
            raise InvalidMarkError("Enter the currect mark out of 100")
        with open("data/students.txt", "a") as file:
            file.write(f"{name},{mark}\n")
            print("===== SUCCESS FULLY ADDED THE STUDENT TO THE DATA BASE =====")

    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Enter the currect value")
    except InvalidMarkError as e:
        print(e)


def displayAllStudents():
    try:
        print("===== STUDENT RECORD =====")
        with open("data/students.txt", "r") as file:
            for content in file:
                line = content.strip()
                name, mark = line.split(",")
                print(f"Name: {name} | Mark: {mark}")
    except FileNotFoundError:
        print("file not found")


def searchStudent():
    name = input("Enter the sudent name : ")
    try:
        with open("data/students.txt", "r") as file:
            flag=0
            for content in file:
                line = content.strip()
                Name, mark = line.split(",")
                if name == Name:
                    flag=1
                    print("===== Found student =====")
                    print(f"Name : {Name} | Mark : {mark}")
                    return 
            if flag==0:
                print("===== Student not in the data base please register the student first ======")

    except FileNotFoundError:
        print("file not found")
