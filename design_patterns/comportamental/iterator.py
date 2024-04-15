from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, item: Any) -> None:
        self._items.append(item)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    my_list = MyList()

    my_list.add('romario')
    my_list.add('luiz')
    my_list.add('maria')

    for value in my_list:
        print(value)
