"""
LV2. 카펫
[https://school.programmers.co.kr/learn/courses/30/lessons/42842]

해석:
- 카펫의 조건: 중앙은 노란색으로 칠해져 있고, 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
- 즉 중앙 부분이 (w, h)라면, 총 카펫의 모양은 (w+2, h+2)가 된다.
- 따라서 문제의 조건은 `w * h = yellow`를 만족하는 카펫의 가로와 세로를 구하는 것이다.

풀이:
[solution 1: 공약수들을 대상으로 조건부 탐색 진행]
1. 갈색(B)의 개수와 노란색(Y)의 개수를 더한다. (K = B+Y)
2. 1부터 K의 제곱근까지 1씩 증가 시키며 전체 카펫에 대한 가로(w)와 세로(h)를 구한다.
3. 이때 w-2와 h-2는 중앙 부분의 가로와 세로 길이이며, 다음 조건에 만족하는 [w, h]를 반환한다.
    -> (w-2)*(h-2) == yellow


[solution 2: 근의 공식을 이용하여 찾는 방식]
- 위 문제에 주어진 수식을 정리 하면 아래와 같다.
    -> w * h = yellow, (w+2) * (h+2) = brown + yellow

- 이때 2번째 식을 w에 대한 식으로 정리 하면 아래와 같다.
    -> 2w^2 - (brown-4)x + 2yellow = 0

- 이는 2차 방정식 'ax^2 + bx + c = 0'과 동일한 형태이므로, 이를 w에 대한 근의 공식으로 정리할 수 있다.
    -> w = (-b + sqrt(b^2 - 4ac)) / 2a
    -> h = (-b - sqrt(b^2 - 4ac)) / 2a

    [a = 2, b = -(brown-4), c = 2yellow]

- 따라서 정답은 [w + 2, h + 2]가 된다.
"""
from math import sqrt, ceil


def solution1(brown, yellow):
    br = brown + yellow

    for w in range(2, ceil(sqrt(br)) + 1):
        h = br // w

        if (w - 2) * (h - 2) == yellow:
            return sorted([w, h], reverse=True)


def solution2(brown, yellow):
    w, h = quadratic(2, -(brown - 4), 2 * yellow))
    return [w + 2, h + 2]


def quadratic(a, b, c):
    """근의 공식 계산"""
    d = (b ** 2) - (4 * a * c)
    quad1 = ceil((-b + sqrt(d)) / (2 * a))
    quad2 = ceil((-b - sqrt(d)) / (2 * a))
    return quad1, quad2
