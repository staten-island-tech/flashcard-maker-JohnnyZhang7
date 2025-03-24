""" import json

class Car:
    def __init__(self, make, model, year, image=None):
        self.make = make
        self.model = model
        self.year = year
        self.image = image
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image}
    
my_car = Car("Toyota", "Camry", 2023, "camry_image.jpg")
print(my_car.display_info())  # Output: 2023 Toyota Camry """

class teacher:
    def __init__(self, word, key):
        self.word = word
        self.key = key
    def display_info(self):
        return {"word": self.word}

teachers = [
    teacher("")
]

""" #LESSON ON CLASS
class Merchant:
     def __init__(self, name, products):
        self.name = name
        self.products = products
     def sell(self, item):
         self.products.remove(item)
         print(self.products)
Rachel = Merchant("Rachel", ["Apples", "Oranges", "Human"])
Kammy = Merchant("Kammy", ["Penguins", "Whales", "Capybaras"])
print(Rachel.sell("Human"))
print(Kammy.sell("Capybaras")) """