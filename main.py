# decorator

def decor(fun):
    def inner():
        a = fun()
        add = a + 5
        return add

    return inner


def num():
    return 10


result_fun = decor(num)
print(result_fun())



# 간단하게 만들어 보자 @함수 는 아래 함수를 감싼다. 즉, 아래 함수를 @함수에 넣어줘!
@decor
def num():
    return 10

print(num())