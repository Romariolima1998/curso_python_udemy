from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self):
        ''' template method '''

        self.hook_before_add_ingretients()
        self.add_ingrentients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingretients(self): pass

    def cut(self):
        print(f'{self.__class__.__name__} cortando pizza')

    def serve(self):
        print(f'{self.__class__.__name__} servindo pizza')

    @abstractmethod
    def add_ingrentients(self): pass

    @abstractmethod
    def cook(self): pass


class AModa(Pizza):
    def add_ingrentients(self):
        print('AModa: adicionando igredientes presunto, queijo')

    def cook(self):
        print('AModa: cozinhando por 20min no forno')


class Calabresa(Pizza):
    def hook_before_add_ingretients(self):
        print('Calabresa: escolhendo massa com borda recheada')

    def add_ingrentients(self):
        print('Calabresa: adicionando igredientes presunto, queijo, calabresa')

    def cook(self):
        print('Calabresa: cozinhando por 20min no forno')


if __name__ == '__main__':
    a_moda = AModa()
    a_moda.prepare()

    print()
    calabresa = Calabresa()
    calabresa.prepare()
