from array import *
# import array

stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("Array After Insert")

# insert
stu_roll.insert(1, 106)
stu_roll.insert(3, 107)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("Array After Remove")

# remove
stu_roll.remove(107)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("Array After Pop")

# pop
stu_roll.pop()
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("Array After Pop(n)") # n번째 요소 삭제
# pop
stu_roll.pop(2)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1