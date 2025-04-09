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

    #def equation(self, subjects):
        #self.subject.append(subjects)
        #return(self.subject)
""" try:
    with open("teach.json", "r") as file:
        sentences_data = json.load(file)
except FileNotFoundError:
    sentences_data = [] """
import json
import random

class teacher:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def to_dict(self):
        return{"question": self.question, "answer": self.answer}

teachers = []
while True:
    question = input("enter your question")
    if question == "exit":
        break
    answer = input("enter the answer")
    teacher_teacher = teacher(question, answer)
    teachers.append(teacher_teacher)

sentences_data = [teacher.to_dict() for teacher in teachers]
random.shuffle(teachers) 
with open("teach.json", "w") as file:
    json.dump(sentences_data, file, indent = 4)

""" new_subject = input(teacher("what is 48 + 56", "104"))
sentences_data.append(new_subject.to_dict()) """


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
    question_list = input(f"question: {card['question']}")
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

""" teacher("what is 5 * 2", "10"),
teacher("what is 15 - 3", "12"),
teacher("what is 7 + 8", "15"),
teacher("what is 25 * 4", "100"),
teacher("what is 100 / 5", "20"),
teacher("what is 18 + 22", "40"),
teacher("what is 56 / 7", "8"),
teacher("what is 3 * 14", "42"),
teacher("what is 100 - 37", "63"),
teacher("what is 9 * 6", "54"),
teacher("what is 50 + 25", "75"),
teacher("what is 72 / 9", "8"),
teacher("what is 12 * 7", "84"),
teacher("what is 36 / 4", "9"),
teacher("what is 10 + 10", "20"),
teacher("what is 80 - 50", "30"),
teacher("what is 14 * 3", "42"),
teacher("What is the capital city of France?", "Paris"),
teacher("Which continent is known as the 'Dark Continent'?", "Africa"),
teacher("What is the longest river in the world?", "Amazon River"),
teacher("Which country has the largest population?", "China"),
teacher("What is the smallest country in the world by land area?", "Vatican City"),
teacher("Which ocean is the largest by surface area?", "Pacific Ocean"),
teacher("What is the capital city of Japan?", "Tokyo"),
teacher("Which mountain range separates Europe and Asia?", "Ural Mountains"),
teacher("What is the largest desert in the world?", "Sahara Desert"),
teacher("Which country is both an island and a continent?", "Australia"),
teacher("What is the capital city of Canada?", "Ottawa"),
teacher("Which river is the lifeblood of Egypt?", "Nile River"),
teacher("What is the largest island in the Caribbean?", "Cuba"),
teacher("Which country has the most official languages?", "South Africa"),
teacher("Which continent is the Sahara Desert located on?", "Africa"),
teacher("What is the name of the imaginary line that divides the Earth into the Northern and Southern Hemispheres?", "Equator"),
teacher("Which country is known as the Land of the Rising Sun?", "Japan"),
teacher("What is the capital city of Russia?", "Moscow"),
teacher("Which sea is the largest inland body of water?", "Caspian Sea"), """

