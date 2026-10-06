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


st1 = Student("yousaf", 100, "cse")
st2 = Student("hashil", 77, "mmm")
