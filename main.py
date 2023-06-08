# Example 1
def add(x, y):
    z = x + y
    print("Addtion: ", z)


add(5, 2)


# Example 2
def add(*num):
    z = sum(num)
    print("Addition All: ", z)


add(2, 2, 2, 2, 2, 2, 2, 2)


# Example 3
def add(x, *num):
    z = x + num[0] + num[1]
    print("Addition x All: ", z)


add(5, 2, 4, 5)
