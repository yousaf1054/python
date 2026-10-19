class Car():
    def __init__(self):
        self.engin = Engin()

    def start(self):
        self.engin.engin_start()
        print("car started")

    def stop(self):
        self.engin.engin_stop()
        print("car stoped")


class Engin():
    def engin_start(self):
        print("engin started")

    def engin_stop(self):
        print("engin stoped")


car1=Car()
car1.start()