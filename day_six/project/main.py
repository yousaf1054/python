from students.student import addStudent, displayAllStudents, searchStudent
while True:
    print("===== MENU =====")
    print("1. ADD STUDENT")
    print("2. DISPLAY ALL STUDENT")
    print("3. SEARCH STUDENT")
    print("4. EXIT")
    print("=================")
    print("\n\n")
    option=int(input("ENTER THE OPTION YOU WANT :: "))
    if option==1:
        addStudent()
    elif option==2:
        displayAllStudents()
    elif option==3:
        searchStudent()
    elif option==4:
        break
    else:
        print("ENTER VALID OPTIONS FROM THE LIST")
    