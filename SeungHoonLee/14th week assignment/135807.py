"""
LV2. 숫자 카드 나누기
[https://school.programmers.co.kr/learn/courses/30/lessons/135807]

- 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a의 값을 구하기
- 조건을 만족하는 a가 없다면, 0
- arrayA와 arrayB에는 중복된 원소가 있을 수 있음
    - 중복된 원소가 존재하는 경우, 조건에 만족하는 경우가 없기 때문에 답은 0이 됨
"""
import math
from functools import reduce


def solution(arrayA, arrayB):
    arrA, arrB = set(arrayA), set(arrayB)

    if any(item in arrA for item in arrB):
        return 0

    answer = 0

    if not is_divisible(arrB, key := (gcd(arrA))):
        answer = key

    if not is_divisible(arrA, key := (gcd(arrB))):
        answer = max(answer, key)

    return answer


def gcd(arr):
    return reduce(lambda acc, el: math.gcd(acc, el), arr, 0)


def is_divisible(arr, key):
    return any(item % key == 0 for item in arr)
