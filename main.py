# def val(lst):
    print("inside Function Before Append", lst, id(list))
    lst.append(4)
    print("inside Function Before Append", lst, id(list))

list = [1, 2, 3]
print("Before Calling Function: ", list, id(list))
val(list)
print("After Calling Function: ", list, id(list))


def val2(x):
    print("Inside : ", id(x))
    x += 1
    print("Inside After : ", id(x))

x = 10
print("Before Calling Function: ", x, id(x))
val2(x)
print("After Calling Function: ", x, id(x))