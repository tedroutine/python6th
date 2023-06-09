class Mobile:
    fp = 'yes'



realme = Mobile()  # Mobile() : 생성자 함수이고, 인스턴스에 메모리를 할당하는 것
redme = Mobile()
geek = Mobile()

print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

Mobile.fp = 'no'
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

realme.fp = 'idk' # 인스턴스 네임스페이스
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)