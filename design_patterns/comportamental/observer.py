from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    ''' interface observable '''
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
    ''' observable '''

    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state = {**self._state, **state_update}

        if self._state != new_state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
            print()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__

        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')

# podem ser criado varios outros observer como notebooks smartfones e outros
# cada observer usa os dados do observable como quiser


if __name__ == '__main__':
    weather_station = WeatherStation()

    smartphone1 = Smartphone('xiaomi', weather_station)
    smartphone2 = Smartphone('sansung', weather_station)

    weather_station.add_observer(smartphone1)
    weather_station.add_observer(smartphone2)

    weather_station.state = {'temperature': '30'}
    weather_station.state = {'temperature': '25'}

    weather_station.remove_observer(smartphone2)

    weather_station.reset_state()
