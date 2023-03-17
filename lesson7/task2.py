"""
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def set_mass(self, mass):
        self.mass = mass

    def set_fatness(self, fatness):
        self.fatness = fatness

    def calculation(self):
        return self._length * self._width * self.mass * self.fatness


road = Road(20, 5000)
road.set_mass(25)
road.set_fatness(0.05)
print(road.calculation())
