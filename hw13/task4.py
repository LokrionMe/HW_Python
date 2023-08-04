class User:

    def __init__(self, name: str, user_id: int, level: int = None) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self) -> str:
        return f"Name: {self.name}, id: {self.user_id}, level: {self.level}"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.user_id == other.user_id
