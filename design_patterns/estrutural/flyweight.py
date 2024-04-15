from __future__ import annotations
from typing import List, Dict


class Cliente:
    ''' context'''

    def __init__(self, name: str) -> None:
        self.name = name
        self.addresses: List = []

        # extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def list_addresses(self) -> None:
        for address in self.addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    ''' flyweight'''

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self.street = street
        self.neighbourhood = neighbourhood
        self.zip_code = zip_code

    def show_address(self, number: str, detail: str):
        print(
            self.street, number, self.neighbourhood, detail,
            self.zip_code
        )


class AddressFactory:
    _addresses: Dict = {}

    def get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self.get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('usando objeto ja criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('criando objeto')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street=' vila velha', neighbourhood='HUmaita', zip_code='29000900')

    a2 = address_factory.get_address(
        street=' vila velha', neighbourhood='HUmaita', zip_code='29000900')

    romario = Cliente('romario')
    romario.address_number = '10'
    romario.address_details = 'casa'
    romario.add_address(a1)

    romario.list_addresses()
