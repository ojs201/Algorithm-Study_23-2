"""
LV2. 하노이의 탑
[https://school.programmers.co.kr/learn/courses/30/lessons/12946]
"""


def solution(n):
    answer = []

    def hanoi(n, start, dest, via):
        nonlocal answer

        if n == 1:
            answer.append([start, dest])
        else:
            hanoi(n - 1, start, via, dest)
            answer.append([start, dest])
            hanoi(n - 1, via, dest, start)

    hanoi(n, 1, 3, 2)
    return answer
