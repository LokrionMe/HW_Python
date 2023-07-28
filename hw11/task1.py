# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

class MyString(str):
    """Создаем строку с обозначением автора и временем создания"""

    def __init__(self, string, author: str) -> None:
        from time import time
        self.string = string
        self.author = author
        self.time = time()

    def __new__(cls, *args, **kwargs):
        instance = str().__new__(cls, args[0])
        return instance

    def __str__(self) -> str:
        return f"String: {self.string}, author:{self.author}, time: {self.time}"


string_one = MyString("Hello ", "lokrion")
string_two = MyString("world", "lokrion")
string_three = MyString(5, "Alex")
print(string_one)
print(string_two)
print(string_one.upper() + string_two + string_three)
print(help(MyString))
