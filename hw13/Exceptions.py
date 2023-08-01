class BasicException(Exception):
    pass


class LevelError(BasicException):
    def __str__(self) -> str:
        return 'Level is low'


class AccessError(BasicException):
    def __str__(self) -> str:
        return 'Invalid user' 