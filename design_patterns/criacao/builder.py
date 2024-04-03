from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self): pass

    @abstractmethod
    def add_lastname(self): pass

    @abstractmethod
    def add_age(self): pass

    @abstractmethod
    def add_phone(self): pass

    @abstractmethod
    def add_address(self): pass


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone_numbers):
        self._result.phone_numbers.append(phone_numbers)
        return self

    def add_address(self, addresses):
        self._result.addresses.append(addresses)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

# pelos metosdos add_ retornar self podemos fazer o encadeamento
    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_age(age)
        return self._builder.result

# encadeamento é chaar um metodo atras do outro
    def with_address(self, firstname, lastname, address):
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('romario', 'lima', 25)
    print(user1)

    user2 = user_director.with_address('maria', 'miranda', 'Av Paulista')
    print(user2)
