from abc import ABC, abstractmethod
import csv
from pprint import pprint
import pandas as pd

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    # @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

cupcake_1 = Cupcake('Super Chocolate', 4.99, 'Chocolate', 'Chocolate', 'Chocolate Mousse')

cupcake_1.add_sprinkles('Chocolate', 'White Chocolate Shavings')

# print(cupcake_1.sprinkles)

cupcake_2 = Mini('Vanilla Swirl', 1.99, 'Marbled', 'Choco-Swirl')
# print(cupcake_2.name)
# print(cupcake_2.price)
# print(cupcake_2.size)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# read_csv("sample.csv")

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def append_to_csv(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

#testing functions

# append_to_csv('sample.csv', cupcake_1)
# read_csv('sample.csv')

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
    
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake['name'] == name:
            return cupcake
    return None
    
def add_cupcake_dictionary(file, cupcake):
    with open(file, 'a', newline="\n") as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        print(cupcake)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def order_price(file):
    price = 0
    for cupcake in get_cupcakes(file):
        price += float(cupcake['price'])
    return round(price, 2)

def remove_cupcake(file, cupcake):
    df = pd.read_csv(file)
    df = df[df.name != cupcake['name']]
    df.to_csv(file, index=False)