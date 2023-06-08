# 제너레이터

def fibonacchi_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

fs = fibonacchi_generator(10)

for num in fs:
    print(num)