"""
LV2. 점 찍기
[https://school.programmers.co.kr/learn/courses/30/lessons/140107]


- 두 점 사이의 거리 공식을 활용한다.
- (0,0)에서 (ak,bk) 사이의 거리가 d보다 작거나 같아야 한다.

    d >= sqrt((ak)^2 + (bk)^2)
    d^2 >= (ak)^2 + (bk)^2
    ...
    : b = sqrt(d^2 - (ak)^2) / k

- 따라서 매번 ak에 따른 b값을 더해 주면 답을 구할 수 있다.
"""
from math import sqrt


def solution(k, d):
    answer = 0
    for ak in range(0, d+1, k):
        answer += int(sqrt(d**2 - ak**2)) // k + 1
    return answer
