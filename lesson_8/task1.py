'''
реализовать дескрипторы для любых двух классов
'''

from datetime import date as d

'''
descriptors
'''


class PreviousDateDescriptor:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        curr_date = d.today()
        value_date = d.fromisoformat(value)
        if value_date > curr_date:
            raise Exception(f'дата не может быть выше текущей {value} > '
                            f'{curr_date}')
        instance.__dict__[self.my_attr] = value_date


class NoneNegativeDescriptor:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value <= 0:
            raise Exception(f"значение не может быть 0 или отрицательным, "
                            f"значение:{value}")
        instance.__dict__[self.my_attr] = value


class MarkDescriptor:
    mark_list = ["bmv", "mazda"]

    def __init__(self, mark_attr):
        self.mark_attr = mark_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.mark_attr]

    def __set__(self, instance, value):
        if value not in self.mark_list:
            raise Exception(f"марка автобиля {value} не существует в списке "
                            f"марок {self.mark_list}")
        instance.__dict__[self.mark_attr] = value


'''
two simple classes Car and Animal  
'''


class Car:
    mark = MarkDescriptor('mark')
    creation_date = PreviousDateDescriptor('creation_date')
    max_speed = NoneNegativeDescriptor('max_speed')
    engin_power = NoneNegativeDescriptor('engin_power')

    def __init__(self, max_speed, engin_power):
        self.max_speed = max_speed
        self.engin_power = engin_power


class Animal:
    weight = NoneNegativeDescriptor('weight')
    speed = NoneNegativeDescriptor('speed')
    birth_date = PreviousDateDescriptor('birth_date')

    def __init__(self, name, birth_date):
        self.birth_date = birth_date
        self.name = name


car = Car(1, 1)
car.model = "bmv"
car.creation_date = "2022-12-04"

# exceptio raised Exception: дата не может быть выше текущей 2034-12-04 >
# 2023-03-23
animal = Animal("Goose", "2034-12-04")