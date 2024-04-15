from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    '''subject interface'''
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    '''real subject'''

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # simulando requisiçao no bd
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)
        return [
            {'rua': 'nestor gomes', 'numero': 500}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)
        return {'cpf': '111-222-333-44', 'rg': 'br111'}


class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == '__main__':
    romario = UserProxy('romario', 'lima')

    print(romario.firstname)

    print(romario.get_addresses())
    print(romario.get_all_user_data())

    for i in range(50):
        print(romario.get_addresses())
        print(romario.get_all_user_data())
