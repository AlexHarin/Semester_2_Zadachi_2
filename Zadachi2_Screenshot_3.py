class TriangleChecker:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            self.result = "С отрицательными числами ничего не выйдет!"
        elif type(a) != int or type(b) != int or type(c) != int:
            self.result = "Нужно вводить только числа!"
        else:
            if a + b > c and a + c > b and b + c > a:
                self.result = "Ура, можно построить треугольник!"
            else:
                self.result = "Жаль, но из этого треугольник не сделать."

    def is_triangle(self):
        return self.result
tc = TriangleChecker(8, 10, 14)
print(tc.is_triangle())
