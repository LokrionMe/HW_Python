# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    """
    Создаем класс прямоугольник со сторонами length и width
    используются функции:
        perimeter: вычисляет периметр, возвращает класс Rectangle
        square: вычисляет площадь, возвращает класс Rectangle
    """

    def __init__(self, length, width) -> None:
        self.width = width
        self.length = length

    def __str__(self) -> str:
        return f"Длина = {self.length}, ширина = {self.width}"

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __add__(self, other):
        sum_length = self.length + other.length
        perimeter = self.perimeter() + other.perimeter()
        rect = Rectangle(sum_length, perimeter/2 - sum_length)
        return rect
    
    def __sub__(self, other):
        perimeter = abs(self.perimeter() - other.perimeter())
        if perimeter <= 2:
            return "Прямоугольник не может существовать"
        else:
            if self.length == other.length:
                return Rectangle(self.length, perimeter/2 - self.length)
            else:
                sub_length = abs(self.length - other.length)
                return Rectangle(sub_length, perimeter/2 - sub_length)

    def square(self):
        return self.length * self.width

    def __eq__(self, other) -> bool:
        return self.square() == other.square()
    
    def __ge__(self, other) -> bool:
        return self.square() >= other.square()
    
    def __lt__(self, other) -> bool:
        return self.square() < other.square()


rect_one = Rectangle(1, 4)
rect_two = Rectangle(4, 1)
print(rect_one)
print(rect_two)
print(rect_two + rect_one)
print(rect_one == rect_two)
print(rect_one >= rect_two)
print(rect_one < rect_two)
print(rect_one > rect_two)
print(rect_one <= rect_two)
print(rect_one != rect_two)