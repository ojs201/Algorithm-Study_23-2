"""
LV2. 삼각 달팽이
[https://school.programmers.co.kr/learn/courses/30/lessons/68645]

[삼각형] (e.g. n = 4)
[
    [0]
    [0, 0]
    [0, 0, 0]
    [0, 0, 0, 0]
]

풀이:
1. 1부터 n까지 달팽이 채우기를 진행한다.

    [달팽이 채우기 1바퀴 당 동작]
    - 위 -> 아래: i가 +1씩 증가
    - 왼 -> 오 : j가 +1씩 증가
    - 아래 -> 위: i와 j가 -1씩 감소

    e.g. 1번째 바퀴 실행 (e.g. n = 4, i = 1, 위 -> 아래)
        for _ in range(i, n):
            answer[x++][j] = curr++; (이때, x = 0 ~ n-1)

2. 2차원 배열을 1차원으로 변환한 후 반환한다.
"""


def solution(n):
    answer = [[0] * num for num in range(1, n + 1)]
    num = 1
    x, y = -1, 0

    for i in range(n):
        for _ in range(i, n):

            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1

            answer[x][y] = num
            num += 1

    return sum(answer, [])
