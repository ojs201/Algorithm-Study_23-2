"""
LV2. 이진 변환 반복하기
[https://school.programmers.co.kr/learn/courses/30/lessons/70129]
"""


def solution(s):
    transforms, removals = 0, 0

    while s != '1':
        removals += (len(s) - s.count('1'))
        transforms += 1

        nums_one = s.count('1')
        s = bin(nums_one)[2:]

    return [transforms, removals]
