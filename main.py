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

new_set = a.copy()
new_set.add(100)
print(new_set)

# 교집합 : intersaction
intersactoin_a = a.intersection(new_set)
print("intersactoin_a : ", intersactoin_a)

# 합집합 : union
union_a = a.union(new_set)
print("union_a : ", union_a)

# 차집합 : difference : A 기준으로 B와 다른 것만 return
difference_a = new_set.difference(a)
print(a)
print(new_set)
print("difference_a : ", difference_a)

# issubset : 하위 집합, issuperset : 상위 집합
print(a.issubset(new_set))
print(new_set.issuperset(a))

# 대칭 차집합 : symmetric_difference
sym_a = a.symmetric_difference(new_set)
print('symmetric_difference: ', sym_a)





