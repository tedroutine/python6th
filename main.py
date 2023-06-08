fruits = ['apple', 'banana', 'cherry', 'mango']
veges = ["onion", 'garlic']

grocery = fruits + veges
print(grocery)

numbers = [10, 5, 8, 1, 7]
numbers.sort()

print(numbers)

slice_numbers = numbers[1:4]
print(slice_numbers)

numbers_copy = numbers.copy()
print(numbers_copy)
id(numbers_copy)

numbers_clone = numbers[:]
print(numbers_clone)
id(numbers_copy)