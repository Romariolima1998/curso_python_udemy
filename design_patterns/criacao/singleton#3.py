
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)

        print(cls._instances)

        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = 'escuro'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)
