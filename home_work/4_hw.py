# Задача 1

print('Задача 1')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

obj1 = Rectangle(2, 5)
obj2 = Rectangle(10, 10)
obj3 = Rectangle(5, 10)
print(obj1.area(), obj1.perimeter())
print(obj2.area(), obj2.perimeter())
print(obj3.area(), obj3.perimeter())

print('\n')

# Задача 2

print('Задача 2')

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

num1 = Math(10, 20)
print(num1.addition())
print(num1.multiplication())
print(num1.division())
print(num1.subtraction())

print('\n')

# Задача 3

print('Задача 3')

