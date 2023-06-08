def add(**num):  # num: {'a':5, 'b':2, 'c':1. 'd':5}
    z = num['a'] + num['b'] + num['c']
    print('Addition: ', z)


add(a=5, b=5, c=10)
