class Soda:
    def __init__(self, additive):
     self.additive = additive
 
    def show_my_drink(self):
     if self.additive:
         print("Газировка и {ДОБАВКА}")
     else:
         print("Обычная газировка")
soda1 = Soda("лимон")
soda1.show_my_drink()

