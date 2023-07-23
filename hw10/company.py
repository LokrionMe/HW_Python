# я так понял в задании про фабрику, что надо чтобы класс фабрика (в моем случае company)
# принял на вход класс животного и хранил именно класс животного, поэтому я ничего не придумал
# лучше кроме как взять список внутри фабрики и закидывать туда класс Animal, так он хранит 
# любое животное, которое является дочерним от Animal и к нему, если нужно, можно обратиться

class Animal:
    def __init__(self, name: str, age: int, sex: str = 'm') -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return (f"Name - {self.name}, age - {self.age}, sex - {self.sex}")


class Cat(Animal):
    def __init__(self, name: str, age: int, sex: str = 'm') -> None:
        super().__init__(name, age, sex)

    def __str__(self) -> str:
        return super().__str__()


class Dog(Animal):
    def __init__(self, name: str, age: int, sex: str = 'm') -> None:
        super().__init__(name, age, sex)

    def __str__(self) -> str:
        return super().__str__()


class Company:

    def __init__(self) -> None:
        self.animals: list() = []

    def get_list_animals(self) -> list:
        return self.animals

    def add_animal(self, animal: Animal):
        self.get_list_animals().append(animal)

    def __str__(self) -> str:
        return str(list(map(str, self.get_list_animals())))


cat_one = Cat('kuzya', 5)
dog_one = Dog('King', 3)
company_one = Company()
company_one.add_animal(cat_one)
company_one.add_animal(dog_one)
print(company_one)
