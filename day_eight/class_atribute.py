class Student:
    school_name = "MEA engineering college"

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def print_details(self):
        print(
            f"Name : {self.name}\nMark : {self.mark}\nSchool : {self.school_name}")

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    @staticmethod
    def is_valid_mark(mark):
        return 0 < mark <= 100


st1 = Student("yousaf p", 100)
st2 = Student("hashil", 80)

st1.print_details()
st2.print_details()

# Class method
Student.change_school("Python Academy")

print("\nAfter changing the school:")
st1.print_details()
st2.print_details()

# Static method
print("\nMark validation:")
print(Student.is_valid_mark(85))   # True
print(Student.is_valid_mark(0))    # True
print(Student.is_valid_mark(100))  # True
print(Student.is_valid_mark(120))  # False
