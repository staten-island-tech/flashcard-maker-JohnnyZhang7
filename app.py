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


import json
try:
    with open("teach.json", "r") as file:
        sentences_data = json.load(file)
except FileNotFoundError:
    sentences_data = []
class teacher:
    def __init__(self, key, word):
        self.key = key
        self.word = word
    def sentence(self, words):
        self.word.append(words)
        return(self.word)
    def to_dict(self):
        return{"key": self.key, "word": self.word}
"""         part_list_AD = self.word[:1]
        return part_list_AD
AD = teacher("AD", ["very good", "not bad", "very bad"])
print(AD.sentence("")) """ 

teachers = [
    teacher("very good", "to russian"),
    teacher("not bad", "to russian"),
    teacher("very bad", "to russian")
]

sentences_data = [teacher.to_dict() for teacher in teachers]
with open("teachers.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)
new_flash = teacher("")

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