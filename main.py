fruits = ['apple', 'banana', 'cherry', 'mango']

fruits.append('strawberry')

print(fruits)

fruits.insert(0, 'blueberry')

print(fruits)

print(fruits.pop())
print(fruits)
print(fruits.pop(1))
print(fruits)

fruits.insert(0, 'cherry')
print(fruits)
print(fruits.index("cherry"))
fruits.remove("cherry") # 첫 번째 요소만 제거 / 그리고 return 값도 없고 제거 하고 끝
print(fruits.index("cherry"))
print(fruits)
fruits.reverse()
print(fruits)

