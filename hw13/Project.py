# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты –
#   список пользователей проекта и админ проекта.
# Класс имеет следующие методы:
#   Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
#   Метод входа в систему – требует указать имя и id пользователя. Далее метод
#       создает пользователя и проверяет есть ли он в списке пользователей проекта.
#       Если в списке его нет, то вызывается исключение доступа.
#       Если пользователь присутствует в списке пользователей проекта, то пользователь,
#       который входит получает его уровень доступа и становится администратором.
#   Метод добавление пользователя в список пользователей. Если уровень пользователя меньше,
#       чем уровень админа, вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

from Exceptions import AccessError, LevelError
from task4 import User
import json


class Project:
    """Класс project, хранит список юзеров типа: User"""

    def __init__(self, list_users: list = None) -> None:
        if list_users is None:
            self.list_users = []
        self.list_users = list_users
        self.admin: User = None

    @classmethod
    def read_users(cls, filename):
        with open(f'{filename}.json', 'r') as j_file:
            f_dict = json.load(j_file, object_hook=lambda d: {
                int(k): v for k, v in d.items()})
        f_list = [User(u_name, u_id, level) for level, users in f_dict.items()
                  for u_id, u_name in users.items()]
        return Project(f_list)

    def login(self, name: str, u_id: int):
        '''Проверяет существует ли юзер с name и id,
        если находит - админа приравнивает пользователю,
        если нет - прокидывает AccessError'''
        ch_user = User(name, u_id)
        if ch_user in self.list_users:
            self.admin = self.list_users[self.list_users.index(ch_user)]
            return f"Welcome, {ch_user.name}"
        raise AccessError

    def __str__(self) -> str:
        if self.list_users is None:
            return "Empty"
        return '\n'.join(map(str, self.list_users))

    def add_user(self, user: User):
        '''Добавляет пользователя, если админ не None и уровень позволяет'''
        if self.admin is None:
            return "Please login before to try to add users"
        elif self.admin.level >= user.level:
            raise LevelError
        else:
            self.list_users.append(user)
            return "User added"

    def delete_user(self, user: User):
        '''Удаляет пользователя, если админ не None и уровень позволяет'''
        if self.admin is None:
            return "Please login before to try to add users"
        elif self.admin.level >= user.level:
            raise LevelError
        else:
            if user in self.list_users:
                self.list_users.pop(self.list_users.index(user))
                return "User deleted"

    def write_users(self, filename):
        '''Сохраняет список юзеров типа: User в JSON-файл'''
        # вообще эта функция для контексного менеджера, но он пока не реализован
        # однако функция рабочая
        with open(f'{filename}.json', 'w') as j_file:
            f_dict = {i.level: {} for i in self.list_users}
            for i in self.list_users:
                f_dict.get(i.level).update({i.user_id: i.name})
            json.dump(f_dict, j_file)


# Перед запуском, если у вас есть свой json файл, то используйте его, по идеи должно сработать,
# если файла нет или что-то пошло не так, то сначала запустите test.py, он создаст необходимое
test_project = Project().read_users('users')
print(test_project)
a = User('vitalya', 1, 1)
b = User('vitalya', 2, 1)
c = User('egor', 5, 1)
d = User('pasha', 6, 3)
print(test_project.add_user(c))
print(test_project.login('vitalya', 1))
print(test_project.admin)
# # print(test_project.add_user(c)) #Дропает LevelError
print(test_project.add_user(d))
test_project.write_users('users2')
print(test_project.delete_user(d))
# print(test_project.login('vitalya', 2)) #Дропает AccessError
