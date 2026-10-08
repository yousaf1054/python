from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def calculate_bonus(self):
        pass


class Devleoper(Employee):
    def calculate_bonus(self):
        return 10000

    def total_month_salary(self):
        total_salary = self.get_salary()+self.calculate_bonus()
        print(f"toatal amount {self.name} (developer) get :: {total_salary}")


class Manager(Employee):
    def calculate_bonus(self):
        return 15000

    def total_month_salary(self):
        total_salary = self.get_salary()+self.calculate_bonus()
        print(f"toatal amount {self.name} (manager) get :: {total_salary}")

yousaf=Manager("yousaf",50000)
yousaf.total_month_salary()
vasif=Devleoper("vasif",10000)
vasif.total_month_salary()
