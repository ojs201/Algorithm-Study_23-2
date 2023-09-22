"""
LV2. 피보나치 수
[https://school.programmers.co.kr/learn/courses/30/lessons/12945]
"""


def solution(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b % 1234567
