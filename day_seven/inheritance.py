class Student:
    def __init__(self, name, mark, course):
        self.name = name
        self.__mark = mark
        self.course = course

    def display(self):
        print(
            f"Name : {self.name}\nMark : {self.get_mark()}\nCourse : {self.course}")

    def add_mark(self, mark):
        if mark < 0:
            print("the added mark cannot be negative")
        else:
            temp_mark = self.get_mark()+mark
            self.set_mark(temp_mark)

    def exam_status(self):
        if self.get_mark() >= 50:
            print(f"{self.name} is pass")
        else:
            print(f"{self.name} is fail")

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        if mark < 0:
            print("Mark cannot be negative")
        elif mark > 100:
            print("Mark cannot be greater than 100")
        else:
            self.__mark = mark


class CSStudent(Student):
    def __init__(self, name, mark, course, programming_language):
        super().__init__(name, mark, course)
        self.pr_l = programming_language

    def display(self):
        super().display()
        print(f"Programming language:{self.pr_l}")

    def exam_status(self):
        mark = self.get_mark()
        if 90 <= mark <= 100:
            print("Excellent")
        elif 75 <= mark <= 89:
            print("Very Good")
        elif 50 <= mark <= 74:
            print("pass")
        else:
            print("fail")


class MathStudent(Student):

    def exam_status(self):
        mark = self.get_mark()
        if mark < 40:
            print("fail")
        else:
            print("pass")


yousaf = CSStudent("yousaf", 100, "cs", "python")
hashil=MathStudent("hashil",40,"maths")
vasif=Student("VASIF",70,"CS")
students=[yousaf,hashil,vasif]

for student in students:
    student.exam_status()
