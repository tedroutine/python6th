a = {10, 20, 30}
a = {10, 20, 30, 'LikeLion', "bae", 40}
a = {10, 20, 30, 'LikeLion', "bae", 40, 10, 20}

b = set()
a.add(50)
print(a)

print(a, type(a))

a.discard(10)
a.discard(11) # discard는 remove와 달리 삭제할 값이 없으면 그냥 pass
print(a)
