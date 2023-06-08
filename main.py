a = 50

def show():
    a = 10
    print("A: ", a)

show()
print("A: ", a)


def show2():
    global a # global 변수를 가지고 올 수 있음.
    print("show2-A: ", a)
    a = 20
    print("show2-A2: ", a)

show2()
print("A: ", 2)