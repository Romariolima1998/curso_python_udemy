from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print('movendo para cima')

    def right(self) -> None:
        print('movendo para direita')

    def down(self) -> None:
        print('movendo para baixo')

    def left(self) -> None:
        print('movendo para esquerda')


class NewControl():
    def move_top(self) -> None:
        print('movendo para cima')

    def move_right(self) -> None:
        print('movendo para direita')

    def move_down(self) -> None:
        print('movendo para baixo')

    def move_left(self) -> None:
        print('movendo para esquerda')


class ControlAdapter:
    '''adapter control objeto'''

    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()

# segundo metodo


class ControlAdapter2(Control, NewControl):
    ''' adater control class'''

    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == '__main__':
    new_control = NewControl()
    control_object = ControlAdapter(new_control)

    control_object.top()
    control_object.right()
    control_object.down()
    control_object.left()

    # control class
    control_class = ControlAdapter2()

    control_class.top()
    control_class.right()
    control_class.down()
    control_class.left()
