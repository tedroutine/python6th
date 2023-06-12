# class 실습
class Car:
    # 클래스 속성
    wheels = 4

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def drive(self):  # method
        return "The car is Moving!"

    def stop(self):
        return "The car has been stopped."


# 인스턴스 선언
my_car = Car("Kia", "Morning", "Red")

# 인스턴스 속성 사용
print(my_car.make)
print(my_car.model)
print(my_car.color)

# 메소드 호출
print(my_car.drive())
print(my_car.stop())
