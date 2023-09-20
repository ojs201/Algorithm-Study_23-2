"""
LV2. 올바른 괄호
[https://school.programmers.co.kr/learn/courses/30/lessons/12909]
"""


def solution(s):
    parens = 0

    for ch in s:
        parens = parens + 1 if ch == '(' else parens - 1

        if parens < 0:
            break

    return parens == 0
