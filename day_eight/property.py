
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, new_mark):
        if 0 <= new_mark <= 100:
            self.__mark = new_mark
        else:
            raise ValueError("Mark must be between 0 and 100")


student = Student("Yousaf", 85)

# Read the mark
print(student.mark)

# Update the mark
student.mark = 95

print(student.mark)

student.mark = 150

print(student.mark)