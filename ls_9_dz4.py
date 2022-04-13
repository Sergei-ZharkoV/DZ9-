"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат."""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала'.format(self.name))

    def stop(self):
        print('{} остановилась'.format(self.name))

    def turn(self, direction):
        print('{} повернула на{}'.format(self.name, direction))

    def show_speed(self):
        print('{} текущая скорость равна {}'.format(self.name, self.speed))

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Осторожно, вы превысили максимально допустимую скорость!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Осторожно, вы привысили максимально допустимую скорость!')

class PoliceCar(Car):
    pass

my_car = Car(80, 'красный', 'BMW', True)
my_car.show_speed()