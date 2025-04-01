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
    def __init__(self, math, language, answer):
        self.language = language
        self.math = math
        self.answer = answer
    def equation(self, maths):
        self.math.append(maths)
        return(self.math)
    def to_dict(self):
        return{"language": self.language, "math": self.math, "answer": self.answer}

teachers = [
    teacher("what is 5 * 2", "math", "10"),
    teacher("what is 15 - 3", "math", "12"),
    teacher("what is 99 % 9", "math", "11")
]

sentences_data = [teacher.to_dict() for teacher in teachers]
with open("teach.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)
new_math = teacher("what is 48 + 56", "math", "104")
sentences_data.append(new_math.to_dict())

with open("teach.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)

class student:
    def __init__(self, answer, streak):
        self.answer = answer
        self.streak = streak
        self.current_streak = 0
        self.reset_streak = 0
    def streak_streak(self, streaks, points):
        self.points = points
        self.streaks = streaks
        self.points += 1
        self.current_streak += 1
    def to_dict(self):
        return {"answer": self.answer, "streak": self.streak, "current_streak": self.current_streak}

with open("teach.json", "r") as file:
    cards = open("./teach.json", encoding="utf8")   #stole from movie database
    flashcards = json.load(cards)
    
for card in flashcards:
    question_list = input(f"question: {card['math']} ")
    if question_list == card['answer']:
        print("correct")
    Johnny = student("Johnny", ["points", "streaks"])
        print(Johnny.current_streak)
    else:
        print("incorrect")



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

