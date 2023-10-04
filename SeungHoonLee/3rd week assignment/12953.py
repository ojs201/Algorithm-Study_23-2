"""
LV2. N개의 최소공배수
[https://school.programmers.co.kr/learn/courses/30/lessons/12953]

풀이:
-  LCM(N1, N2) = gcd(N1, N2) * N1 * N2 이용
"""
from functools import reduce
from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


def solution(arr):
    return reduce(lcm, arr, arr[0])
