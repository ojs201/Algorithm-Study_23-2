# 피보나치 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def Fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


"""
메모이제이션을 사용한다고 하더라도, 재귀함수를 이용하면 런타임에러 발생
from functools import lru_cache
# 메모이제이션: 이전에 계산한 값을 저장해서 중복된 계산을 피하기

@lru_cache(maxsize=None)
def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo(n - 2) + Fibo(n - 1)

print(Fibo(3))
"""
