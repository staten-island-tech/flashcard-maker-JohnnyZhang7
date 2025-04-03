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
import random
""" try:
    with open("teach.json", "r") as file:
        sentences_data = json.load(file)
except FileNotFoundError:
    sentences_data = [] """
class teacher:
    def __init__(self, subject, language, answer):
        self.language = language
        self.subject = subject
        self.answer = answer
    def equation(self, subjects):
        self.subject.append(subjects)
        return(self.subject)
    def to_dict(self):
        return{"language": self.language, "subject": self.subject, "answer": self.answer}

teachers = []
random.shuffle(teachers)

sentences_data = [teacher.to_dict() for teacher in teachers]
with open("teach.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)
new_subject = input(teacher("what is 48 + 56", "subject", "104"))
sentences_data.append(new_subject.to_dict())

with open("teach.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)

class student:
    def __init__(self, name):
        self.name = name
        self.current_streak = 0
        self.points = 0
    def co_streak(self):
        self.current_streak += 1
    def i_streak(self):
        self.current_streak = 0
    def total_points(self):
        self.points += 1
    def to_dict(self):
        return {"current_streak": self.current_streak, "points": self.points}

with open("teach.json", "r") as file:
    cards = open("./teach.json", encoding="utf8")   #stole from movie database
    flashcards = json.load(cards)
    
Johnny = student("Johnny")
for card in flashcards:
    question_list = input(f"question: {card['subject']}")
    if question_list == card['answer']:
        print("correct")
        Johnny.co_streak()
        if Johnny.current_streak in range(0, 4):
            Johnny.total_points()
        elif Johnny.current_streak in range(4, 7):
            Johnny.total_points()
            Johnny.total_points()
        elif Johnny.current_streak in range(7, 11):
            for i in range(3):
                Johnny.total_points()
        elif Johnny.current_streak in range(11, 21):
            for i in range(4):
                Johnny.total_points()
        elif Johnny.current_streak in range(21, 31):
            for i in range(5):
                Johnny.total_points()
        elif Johnny.current_streak in range(31, 51):
            for i in range(6):
                Johnny.total_points()


    else:
        print("incorrect, your streak has been reset")
        Johnny.i_streak()
        print(f"The answer was: {card['answer']}")
    print(f"Your current streak is {Johnny.current_streak}")
    print(f"Your total points are {Johnny.points}")


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

"""     teacher("what is 5 * 2", "subject", "10"),
    teacher("what is 15 - 3", "subject", "12"),
    teacher("what is 7 + 8", "subject", "15"),
    teacher("what is 25 * 4", "subject", "100"),
    teacher("what is 100 / 5", "subject", "20"),
    teacher("what is 18 + 22", "subject", "40"),
    teacher("what is 56 / 7", "subject", "8"),
    teacher("what is 3 * 14", "subject", "42"),
    teacher("what is 100 - 37", "subject", "63"),
    teacher("what is 9 * 6", "subject", "54"),
    teacher("what is 50 + 25", "subject", "75"),
    teacher("what is 72 / 9", "subject", "8"),
    teacher("what is 12 * 7", "subject", "84"),
    teacher("what is 36 / 4", "subject", "9"),
    teacher("what is 10 + 10", "subject", "20"),
    teacher("what is 80 - 50", "subject", "30"),
    teacher("what is 14 * 3", "subject", "42"),
    teacher("What is the capital city of France?", "subject", "Paris"),
    teacher("Which continent is known as the 'Dark Continent'?", "subject", "Africa"),
    teacher("What is the longest river in the world?", "subject", "Amazon River"),
    teacher("Which country has the largest population?", "subject", "China"),
    teacher("What is the smallest country in the world by land area?", "subject", "Vatican City"),
    teacher("Which ocean is the largest by surface area?", "subject", "Pacific Ocean"),
    teacher("What is the capital city of Japan?", "subject", "Tokyo"),
    teacher("Which mountain range separates Europe and Asia?", "subject", "Ural Mountains"),
    teacher("What is the largest desert in the world?", "subject", "Sahara Desert"),
    teacher("Which country is both an island and a continent?", "subject", "Australia"),
    teacher("What is the capital city of Canada?", "subject", "Ottawa"),
    teacher("Which river is the lifeblood of Egypt?", "subject", "Nile River"),
    teacher("What is the largest island in the Caribbean?", "subject", "Cuba"),
    teacher("Which country has the most official languages?", "subject", "South Africa"),
    teacher("Which continent is the Sahara Desert located on?", "subject", "Africa"),
    teacher("What is the name of the imaginary line that divides the Earth into the Northern and Southern Hemispheres?", "subject", "Equator"),
    teacher("Which country is known as the Land of the Rising Sun?", "subject", "Japan"),
    teacher("What is the capital city of Russia?", "subject", "Moscow"),
    teacher("Which sea is the largest inland body of water?", "subject", "Caspian Sea"), """
