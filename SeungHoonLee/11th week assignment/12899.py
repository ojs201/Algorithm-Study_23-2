"""
LV2. 124 나라의 숫자 [해결 X]
[https://school.programmers.co.kr/learn/courses/30/lessons/12899]
"""


def solution(n):
    t = '412'
    answer = ''

    while n:
        answer += t[n % 3]
        n = n // 3 - 1 if n % 3 == 0 else n // 3

    return answer[::-1]
