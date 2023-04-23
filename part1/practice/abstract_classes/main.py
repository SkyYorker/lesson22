# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

from abc import ABC, abstractmethod

# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.
# Для текстовой анимации Вы можете использовать любые фразы, или воспользоваться нашей подборкой:
# Boat:
#    - Катер громко затарахтел
#    - Двигатель катера чихнул напоследок и заглох
#    - Катер быстро набирает скорость
#    - Катер остановился
# Car:
#    - Машина заурчала двигателем
#    - Машина стоит с заглушенным двигателем
#    - Машина едет к цели назначения
#    - Машина остановилась
# Electroscooter:
#    - Мигнул светодиодом
#    - Мигнул светодиодом дважды
#    - Прохожие в ужасе разбегаются от очередного камикадзе
#    - Торможение об стену прошло успешно


# Корректным решением будет когда экземпляр класса Person смог использовать все три различных транспорта

# в решении класс Transport должен быть унаследован от ABC
# все методы Transport должны быть помечены декоратором @abstractmethod
# Классы Boat, Car, Electroscooter должны быть унаследованы от Transport

# экземпляр класса Person должен поочередно взаимодействовать с объектами Car, Boat, Electroscooter

# код должен выполняться не выбрасывая исключен
class Transport(ABC):


    @abstractmethod
    def start_engine():
        pass

    @abstractmethod
    def stop_engine():
        pass

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def stop():
        pass


class Boat(Transport):
    def start_engine(self):
        print('Двигатель лодки запущен')

    def stop_engine(self):
        print('Двигатель лодки остановлен')

    def move(self):
        print('Лодка плывёт')

    def stop(self):
        print('Лодка остановилась')

class Car(Transport):
    def start_engine(self):
        print('Двигатель машины запущен')

    def stop_engine(self):
        print('Двигатель машины остановлен')

    def move(self):
        print('машины едет')

    def stop(self):
        print('машины остановилась')


class Electroscooter(Transport):
    def start_engine(self):
        print('Двигатель скутер запущен')

    def stop_engine(self):
        print('Двигатель скутер остановлен')

    def move(self):
        print('скутер едет')

    def stop(self):
        print('скутер остановился')

        
class Person():

    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.stop_engine()
        transport.move()
        transport.stop()
# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
