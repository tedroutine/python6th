# lambda & list comprehension

print(list(map(lambda x: x + 10, [1, 2, 3])))

print([n + 10 for n in range(1,11) if n % 2 == 1])