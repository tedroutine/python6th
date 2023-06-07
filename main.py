from array import *
# import array

stu_roll = array('i', [101, 102, 103, 104, 105])

print("array index() method")
print(stu_roll.index(102))

print("extend() method")
arr = array('i', [201, 202, 203, 204, 205])
stu_roll.extend(arr)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("reverse() method")
stu_roll.reverse()
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1
