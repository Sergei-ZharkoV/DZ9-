"""5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка рисует')


class Pencil(Stationery):
    def draw(self):
        print('Маркер рисует')

class Handle(Stationery):
    def draw(self):
        print('Карандаш рисует')

my_pen = Pen('ручка')
my_pencil = Pencil('маркер')
my_handle = Handle('карандаш')

my_pen.draw()
my_pencil.draw()
my_handle.draw()

