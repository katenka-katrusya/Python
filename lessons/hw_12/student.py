# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
from functools import reduce
from pathlib import Path


class Validate:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть текстом')
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = Validate()
    surname = Validate()
    patronymic = Validate()
    _lessons = None

    def __init__(self, surname: str, name: str, patronymic: str, lessons: Path):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.lessons = lessons

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, less: Path):
        if self.lessons is not None:
            raise AttributeError(f'Список предметов уже определён')
        self._lessons = {"lessons": {}}
        with open(less, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons["lessons"][row[0]] = {"estimates": [],
                                                    "tests": [],
                                                    "middle_estimate_test": None}
        self._lessons["middle_estimate"] = None

    def new_estimate(self, name_of_lesson: str, number: int, type_est: str = "less"):
        if name_of_lesson not in self.lessons["lessons"].keys():
            raise AttributeError("Предмет не изучается данным студентом")
        if type_est == "less":
            if number < 2 or number > 5:
                raise ValueError("Оценка вне допустимого диапазона (2-5)")
            self.lessons["lessons"][name_of_lesson]["estimates"].append(number)
            self.lessons["middle_estimate"] = self.middle_estimate(self.lessons)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise ValueError("Оценка вне допустимого диапазона (0-100)")
            self.lessons["lessons"][name_of_lesson]["tests"].append(number)
            self.lessons["lessons"][name_of_lesson]["middle_estimate_test"] = \
                reduce(lambda x, y: x + y, self.lessons["lessons"][name_of_lesson]["tests"]) / \
                len(self.lessons["lessons"][name_of_lesson]["tests"])

    @staticmethod
    def middle_estimate(lessons: dict):
        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["estimates"]) for name in lessons["lessons"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):
        result = f'''Student
        Полное имя = "{self.surname} {self.name} {self.patronymic}",
        Средний балл = {self.lessons["middle_estimate"]}\n'''
        for key, value in self.lessons["lessons"].items():
            result += f'{key}={value["middle_estimate_test"]}\n'

        return result


if __name__ == '__main__':
    m = Student("Смирнова", "Елена", "Ивановна", Path('lessons.csv'))
    # print(m)
    m.new_estimate("Биология", 5)
    m.new_estimate("Английский", 5)
    m.new_estimate("Физика", 2)
    m.new_estimate("Физика", 4)
    m.new_estimate("Математика", 4)
    m.new_estimate("Биология", 4)
    m.new_estimate("Английский", 5)
    m.new_estimate("Физика", 3)
    m.new_estimate("Физика", 2)
    m.new_estimate("Математика", 4)
    m.new_estimate("Математика", 61, "test")
    m.new_estimate("Математика", 78, "test")
    m.new_estimate("Биология", 79, "test")
    m.new_estimate("Биология", 93, "test")
    m.new_estimate("Химия", 95, "test")
    m.new_estimate("Химия", 74, "test")
    m.new_estimate("Английский", 78, "test")
    m.new_estimate("Английский", 89, "test")
    m.new_estimate("Физика", 71, "test")
    print(m)