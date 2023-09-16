"""
LV2. 최댓값과 최솟값
[https://school.programmers.co.kr/learn/courses/30/lessons/12939]
"""


def solution(s):
    s = list(map(int, s.split()))
    s_min, s_max = str(min(s)), str(max(s))
    return s_min + ' ' + s_max
