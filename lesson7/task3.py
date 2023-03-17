"""
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через
перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""
class Worker:
    def __str__(self):
        return str(f"{self.name} {self.surname} {self.position} "
                   f"{self._income}")

    def __init__(self,wage,bonus):
        self.name = ""
        self.surname = ""
        self.position =""
        self._income={"wage": wage,"bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return str(f"{self.name} {self.surname} {self.position}")
    def get_total_income(self):
       return self._income.get("wage") + self._income.get("bonus")
worker = Position(100,50)
worker.name = 'Иван'
worker.surname = 'Иванов'
worker.position = 'менеджер'
print(worker.get_full_name())
print(worker.get_total_income())
print(worker)