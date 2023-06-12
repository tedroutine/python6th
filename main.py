# multi inheritance class -> 복잡도 증가해서 잘 안쓰는 것이 좋고, 나의 Class를 다중 상속으로 받는건 잘못되었다. Class를 잘 만들면 됨

class Engine:
    def start(self):
        return "Engine started"
s
    def stop(self):
        return "Engine stopped"


class Wheels:
    def rotate(self):
        return "Wheels are rotating"


# 다중 상속
class Car(Engine, Wheels):
    pass


my_car = Car()
print(my_car.start())
print(my_car.stop())
print(my_car.rotate())
