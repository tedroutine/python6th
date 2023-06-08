a = 50


def show():
    x = 10
    print(x)
    print(a)


show()

print("global a : ", a)

i = 0


def myfun():
    a = i + 1
    print("My Function", a)  # read local variables first


myfun()
print("global a : ", a)

i = 0


def myfun2():
    t = 0
    t = t + 1  # global 변수와 local 변수가 같아서 오류가 생긴다. global 변수를 read할 수 있지만 로컬과 같았을 때는 충돌
    print(t)


myfun2()
