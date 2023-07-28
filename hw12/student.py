# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра.
#       Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и
#       по оценкам всех предметов вместе взятых.
import csv


class CheckName:
    """
    Дескриптор на проверку имени, фамилии, отчества
    Проверяет каждую позицию отдельно
    Используется метод validate, как проверка
    """

    def __init__(self) -> None:
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, string):
        self.validate(string)
        setattr(instance, self.param_name, string)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалить')

    def validate(self, string):
        if not string.isalpha():
            raise TypeError(
                f'"{self.param_name}" параметр должно включать только буквы')
        if not string.istitle():
            raise ValueError(
                f'"{self.param_name}" параметр должен включать первую заглавную букву')


class Range:
    """
    Дескриптор на проверку значения
    Принимает минимальное и максимальное значение
    Используется метод validate, как проверка
    """

    def __init__(self, min_val, max_val) -> None:
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, check_list):
        self.validate(check_list)
        setattr(instance, self.param_name, check_list)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалить')

    def validate(self, check_list):
        for i in check_list:
            if not isinstance(i, int):
                raise TypeError(
                    f'Значение "{self.param_name}" должно быть целым')
            if i < self.min_val:
                raise ValueError(
                    f'Значение "{i}" меньше {self.min_val}')
            if i > self.max_val:
                raise ValueError(
                    f'Значение "{i}" больше {self.max_val}')


class Subject:

    test = Range(0, 100)
    estimation = Range(2, 5)

    def __init__(self, name: str, test: list, estimation: list) -> None:
        self.name = name
        self.test = test
        self.estimation = estimation

    def __str__(self) -> str:
        return f"{self.name}: tests{self.test}, estimations{self.estimation}"


class Student:

    _list_subjects = []
    name = CheckName()
    lastname = CheckName()
    patronymic = CheckName()

    def __init__(self, last_name: str, name: str, patronymic: str) -> None:
        self.name = name
        self.lastname = last_name
        self.patronymic = patronymic
        self.add_subjects()

    def __str__(self) -> str:
        return f'{self.lastname} {self.name} {self.patronymic}'

    def add_subjects(self):
        f_list = []
        with open(f'{self.lastname}{self.name}{self.patronymic}.csv', 'r', newline='') as csv_file:
            csv_file = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            next(csv_file)
            for row in csv_file:
                f_list.append(row)
        for i in f_list:
            name_subject = i[0]
            tests_subject = (
                list(map(int, i[1].replace(" ", '')[1:-1].split(','))))
            estimations_sybject = (
                list(map(int, i[2].replace(" ", '')[1:-1].split(','))))
            self._list_subjects.append(
                Subject(name_subject, tests_subject, estimations_sybject))

    def get_list_subject(self) -> list[Subject]:
        return self._list_subjects

    def average_score_tests(self) -> list:
        """Считает средний бал по тестам каждого предмета отдельно"""
        f_list = []
        for i in self.get_list_subject():
            f_list.append(f'{i.name}:{sum(i.test) / len(i.test)}')
        return f_list

    def average_score_estimations(self) -> float:
        """Считает средний бал по оценкам всех предметов"""
        sum_estimations = 0
        sum_len = 0
        for i in self.get_list_subject():
            sum_estimations += sum(i.estimation)
            sum_len += len(i.estimation)
        return sum_estimations / sum_len

#создал словарь для примера
h = {'History': [[34, 45, 24, 85], [4, 2, 3]], 'Math': [[75, 67], [5, 3, 4]]}
#записал его в csv файл
with open(f'IvanovIlyaPetrovich.csv', 'w', newline='') as csv_file:
    csv_file = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    csv_file.writerow(['Name', 'Test', 'Estimation'])
    for i in h.keys():
        l_string = [i, h[i][0], h[i][1]]
        print(l_string)
        csv_file.writerow(l_string)

a = Student('Ivanov', 'Ilya', "Petrovich")
for i in a.get_list_subject():
    print(i)
print(a.average_score_tests())
print(a.average_score_estimations())
