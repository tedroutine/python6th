# lambda & list comprehension
# lambda

print("1. practice : ", (lambda x: x + 10)(1))

print("2. practice : ", list(map(lambda x: x + 10, [1, 2, 3])))

# key
a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
b = sorted(a)
print("a: ", a)
print("b: ", b)
d = sorted(a, key = lambda x : x[0])
e = sorted(a, key = lambda x : x[1])
# f = sorted(a, key = lambda x : x[2]) : 리스트 값(튜플)에서 인덱스는 0번째, 1번째만 있어서 x[2]가 먹히지 않는다!
g = sorted(a, key = lambda x : x[-1])
print("d: ", d)
print("e: ", e)
# print("f: ", f)
print("g: ", g)






# list comprehension
print("10. practive : ", [n + 10 for n in range(1,11) if n % 2 == 1])