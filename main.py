class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.number = 10

    def __str__(self):
        return f'ParentClass name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('부모 : ', new_number, '만큼 더해야지')
        self.number += new_number


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # 부모 class 바로 가져와서 그대로 받아들임. __init__ 함수 빼고 pass와 같음
        self.name = 'child'

    def __str__(self):
        return f'ChildClass name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('말 안듣는 자식: 고정적으로 5를 더할건데?')
        self.number += 5


parent = ParentClass()
child = ChildClass()
print(parent)
print(child)
print('---------------')

print('7일을 더하세요.')
parent.add_num(7)
child.add_num(7)

print(parent)
print(child)
