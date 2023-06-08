# 재귀 함수
import sys

# 재귀함수에 limit을 거는 함수
sys.setrecursionlimit(3000)

print("default: ", sys.setrecursionlimit(3000))
i = 0
def myfun():
    global i
    i += 1
    print("my function is ", i)
    myfun()

myfun()