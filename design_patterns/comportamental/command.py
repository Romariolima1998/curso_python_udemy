from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    ''' receiver luz inteligente'''

    def __init__(self, name: str, rom_name: str) -> None:
        self.name = name
        self.rom_name = rom_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f' {self.name} in {self.rom_name} is now ON')

    def off(self) -> None:
        print(f'{self.name} in {self.rom_name} is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f' {self.name} in {self.rom_name} is now {self.color}')


class ICommand(ABC):
    '''interface de comandos'''

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    ''' comando concreto'''

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColorCommand(ICommand):
    ''' comando concreto'''

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    ''' invoker '''

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def buttons_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def button_pressed_again(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if self._undos:
            button, action = self._undos[-1]

            if action == 'execute':
                self._buttons[button].undo()
            else:
                self._buttons[button].execute()

            self._undos.pop()


if __name__ == '__main__':
    badroom_light = Light('luz do quarto', 'quarto')
    bathroom_light = Light('luz do banheiro', 'banheiro')

    badroom_light_on = LightOnCommand(badroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)

    badroom_light_blue = LightChangeColorCommand(badroom_light, 'blue')

    remote = RemoteController()
    remote.buttons_add_command('first_button', badroom_light_on)
    remote.buttons_add_command('second_button', bathroom_light_on)
    remote.buttons_add_command('third_button', badroom_light_blue)

    remote.button_pressed('first_button')
    remote.button_pressed_again('first_button')

    remote.button_pressed('third_button')

    print()

    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
