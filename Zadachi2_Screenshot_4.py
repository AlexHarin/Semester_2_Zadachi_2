class Nikola:
    def __init__(self, name, age):
        self.name = "Николай"
        self.age = age
        print(f'Я не {name}, а {self.name} и мне {self.age} лет')

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

nikola = Nikola(name, age)
