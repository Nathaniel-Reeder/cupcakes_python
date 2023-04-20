from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, cake_flavor, frosting_flavor, filling):
        self.name = name
        self.price = price
        self.cake_flavor = cake_flavor
        self.frosting_flavor = frosting_flavor
        self.filling = filling
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, cake_flavor, frosting_flavor):
        self.name = name
        self.price = price
        self.cake_flavor = cake_flavor
        self.frosting_flavor = frosting_flavor
        self.sprinkles = []

cupcake_1 = Cupcake('Super Chocolate', 4.99, 'Chocolate', 'Chocolate', 'Chocolate Mousse')

cupcake_1.add_sprinkles('Chocolate', 'White Chocolate Shavings')

print(cupcake_1.sprinkles)

cupcake_2 = Mini('Vanilla Swirl', 1.99, 'Marbled', 'Choco-Swirl', 'Creme')
print(cupcake_2.name)
print(cupcake_2.price)
print(cupcake_2.size)