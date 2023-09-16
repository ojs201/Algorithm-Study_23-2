"""
LV2. JadenCase 문자열 만들기
[https://school.programmers.co.kr/learn/courses/30/lessons/12951]
"""


def solution(s):
    return ' '.join([jaden_case(w) for w in s.split(" ")])


def jaden_case(s):
    return s if not s else s.capitalize()
