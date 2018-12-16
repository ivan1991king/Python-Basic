# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def area(self):
        self.area = (1 / 2) * math.fabs(((self.x2 - self.x1) * (self.y2 - self.y1)) -\
                                           ((self.x3 - self.x1) * (self.y3 - self.y1)))
        return self.area
    def perimetr(self):
        self.a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.c = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        self.perimetr = self.a + self.b + self.c
        return self.perimetr
    def height(self):
        self.height1 = 2 * self.area / self.a
        self.height2 = 2 * self.area / self.b
        self.height3 = 2 * self.area / self.c
        return [self.height1, self.height2, self.height3]

#Пример
treug1 = triangle(1, 1, -2, 4, -2, -2)
print("Площадь треугольника равна: " + str(treug1.area()))
print("Периметр треугольника равен: " + str(treug1.perimetr()))
print("Высоты треугольника равны: ")
print(treug1.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapecia():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    def ravnob(self):
        #проверим если диагонали равны:
        d1 = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        d2 = math.sqrt((self.x4 - self.x2) ** 2 + (self.y4 - self.y2) ** 2)
        if d1 == d2:
            print("Данная трапеция равнобочная")
            return True
        else:
            print("Данная трапеция НЕ равнобочная")
            return False
    def lenghts(self):
        self.a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) #основание 1
        self.b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.c = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)  #основание 2
        self.d = math.sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
        print(f"Длины сторон трапеции: a={self.a}, b={self.b}, c={self.c}, d={self.d}")
    def perimetr(self):
        self.perimetr = self.a + self.b + self.c + self.d
        print("Периметр трапеции равен: " + str(self.perimetr))
    def area(self):
        area = ((self.a+self.c) / 2) * math.sqrt(self.d**2 - (((self.c - self.a) ** 2 + self.d **2 - self.b ** 2) / (2 * (self.c - self.a)))**2)
        print("Площадь трапеции равна: " + str(area))
#Пример
print('\n')
trap1 = trapecia(2, 4, 4, 4, 5, 1, 1, 1)
trap1.ravnob()
trap1.lenghts()
trap1.perimetr()
trap1.area()


