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
    def __init__(self, math, language):
        self.language = language
        self.math = math
    def sentence(self, maths):
        self.math.append(maths)
        return(self.math)
    def to_dict(self):
        return{"language": self.language, "math": self.math}
"""         part_list_AD = self.math[:1]
        return part_list_AD
AD = teacher("AD", ["very good", "not bad", "very bad"])
print(AD.sentence("")) """ 

teachers = [
    teacher("what is 5 * 2", "math"),       #FOR TOMORROW: PUT THE ANSWER AFTER "MATH"
    teacher("what is 15 - 3", "math"),
    teacher("what is 99 % 9", "math")
]

sentences_data = [teacher.to_dict() for teacher in teachers]
with open("teach.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)
new_math = teacher("what is 48 + 56", "math")
sentences_data.append(new_math.to_dict())

with open("teach.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)

class student:
    def __init__(self, answer):
        self.answer = answer
    def calculate_sum(self, a, b):
        return a + b
    def calculate_subtract(self, a, b):
        return a - b
    def calculate_multiply(self, a, b):
        return a * b
    def calculate_divide(self, a, b):
        if b > 0:
            return a % b
        else:
            return("impossible problem")

with open("teach.json", "r") as file:
    flashcards = file.read()
    print(flashcards)



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