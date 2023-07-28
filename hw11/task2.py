# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    Создаем архив с числом и строкой, по мере поступления
    экземпляров архив расширяется
    """
    list_archive = []
    def __init__(self, numb: int, string: str) -> None:
        self.numb = numb
        self.string = string

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.list_archive.append(args)
        return instance

    def __str__(self) -> str:
        return f"{self.numb}; {self.string}"
    
    def __repr__(self) -> str:
        return f"Archive({self.numb},'{self.string}')"


arc = Archive(5,"five")
print(arc)
print(arc.list_archive)
arc_two = Archive(1,"one")
print(repr(arc_two))
print(arc.list_archive)
