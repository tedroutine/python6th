# 언패킹 : *
# 리스트 앞에 * 있으면 값 하나씩 감싸는 함수 프로퍼티 값에 추가된다.


def add(x, y, z):
    return x + y + z


n = [1, 2, 3]
print(add(*n))
