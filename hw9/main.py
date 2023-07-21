import csv
from random import randint
import json

# учитывая все ваши прошлые комментарии, расписываю что и для чего подробно


def gen_list(n: int):
    # функция, необходимая для создания CSV файла со случайными коэффицентами
    dict_rand = {'a': [], 'b': [], 'c': []}
    for i in range(n):
        dict_rand['a'].append(randint(-10, 10))
        dict_rand['b'].append(randint(-10, 10))
        dict_rand['c'].append(randint(-10, 10))
    with open("data.csv", "w", newline="") as csv_file:
        csvfile = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        csvfile.writerow(dict_rand.keys())
        for i in range(len(dict_rand[list(dict_rand.keys())[0]])):
            f_list = []
            for j in dict_rand.keys():
                f_list.append(dict_rand[j][i])
            csvfile.writerow(f_list)
        print("CSV file is created")


def read_csv(func: callable):
    # декоратор читает CSV файл и сохраняет все решения в список
    cache_list = []

    def wrapper():
        with open("data.csv", "r", newline='') as r_csv:
            reader = csv.reader(r_csv, quoting=csv.QUOTE_NONNUMERIC)
            f_list = []
            for row in reader:
                f_list.append(row)
            print("CSV file is read")
        for z in range(1, len(f_list)):
            a = f_list[z][0]
            b = f_list[z][1]
            c = f_list[z][2]
            cache_list.append(
                f"{a} * x**2 + {b} * x + {c} = 0, solution = {func(a, b, c)}")
        return cache_list
    return wrapper


def save_json(func):
    # декоратор создает JSON файл и сохраняет в него результат
    def wrapper(*args, **kwargs):
        with open('solutions.json', 'w') as writer:
            res = func(*args, **kwargs)
            json.dump(res, writer)
            print("JSON file is created")
    return wrapper


@save_json
@read_csv
def ur(a: int, b: int, c: int):
    if a == 0 and b == 0:
        return "Solution is empty"
    elif a == 0:
        return -c/b
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return "Solution is empty"
        elif d == 0:
            return -b / (2 * a)
        else:
            return ((-b - d ** 0.5)/(2 * a), (-b + d ** 0.5)/(2 * a))


gen_list(1000)  # создаем CSV файл с нужным колличетсвом строчек
ur()  # вытаскивает все строчки из CSV файла, прогоняет их по функции и записывает решения в JSON файл
