# dictionary
stu = {101: 'Kim', 102: 'Bae', 103: 'Hong'}
fees = {'kim': 2000, 'bae':3000, 'hong':8000}
print(stu[101])
print(stu[102])
print(stu[103])

print(fees['kim'])
print(fees['bae'])
print(fees['hong'])

stu[102] = 'Python'
print(stu[102])

stu[104] = 'Like Lion'
print(stu)

del stu[102]
print(stu)

# stu.clear()
# print(stu)

key = (101, 102, 103)
value = 'like lion'
new_stu = dict.fromkeys(key, value)
print(new_stu)

print(stu.items())
print(stu.keys())
print(stu.values(), type(stu.values()))

stu.update({102: 'Lee'})
print(stu)

# dict에서 102(key 값)으로 제거 가능
stu.pop(102)
print(stu)

print(stu.popitem())
print(stu)
print(stu.popitem())
print(stu)
print(stu.popitem())
print(stu)




