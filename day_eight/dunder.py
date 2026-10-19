class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} it price is {self.price}"

    def __add__(self, other):
        return self.price+other.price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


lap = Product("hp pavalion", 50000)
mouse = Product("mouse", 1000)

print(lap)
print(mouse)

print(lap+mouse)
print(lap==mouse)
