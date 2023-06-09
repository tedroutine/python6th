# class

class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"I am {self.name} and my age is {self.age}")


shark = Monster('shark', 7)
wolf = Monster('wolf', 3)
shark.say();
