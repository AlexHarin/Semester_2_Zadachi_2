import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def move_by(self, distance, angle):
        self.x += distance * math.cos(angle)
        self.y += distance * math.sin(angle)

    def is_on_x_axis(self):
        return self.y == 0

    def is_on_y_axis(self):
        return self.x == 0

point1 = Point(1, 2)
point2 = Point(4, 6)

distance = point1.distance_to(point2)
print("Расстояние между точками:", distance)

point1.move_by(3, math.pi/4)
print("Перемещенная точка:", point1.x, point1.y)

print("Точка лежит на оси x:", point1.is_on_x_axis())
print("Точка лежит на оси y:", point1.is_on_y_axis())
