class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def increase_quantity(self, amount):
        """Увеличить количество товара."""
        self.quantity += amount

    def decrease_quantity(self, amount):
        """Уменьшить количество товара."""
        self.quantity -= amount

    def get_total_cost(self):
        """Рассчитать общую стоимость товара."""
        return self.price * self.quantity

product1 = Product("Яблоки", 17, 8)
product2 = Product("Апельсины", 14, 7)

product1.increase_quantity(2)
print("Увеличенное количество яблок:", product1.quantity)

product2.decrease_quantity(1)
print("Уменьшенное количество апельсинов:", product2.quantity)

total_cost1 = product1.get_total_cost()
total_cost2 = product2.get_total_cost()
print("Общая стоимость яблок:", total_cost1)
print("Общая стоимость апельсинов:", total_cost2)
