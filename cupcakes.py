class Cupcake():
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

cupcake_1 = Cupcake('Super Chocolate', 4.99, 'Chocolate', 'Chocolate', 'Chocolate Mousse')

cupcake_1.add_sprinkles('Chocolate', 'White Chocolate Shavings')

print(cupcake_1.sprinkles)