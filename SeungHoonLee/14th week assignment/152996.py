"""
LV2. 시소 짝궁
[https://school.programmers.co.kr/learn/courses/30/lessons/152996]

문제에서 발견할 수 있는 조건은 다음과 같다.
- 시소의 균형을 맞출 수 있는 비율은 1:1, 2:3, 2:4, 3:4 이다.
    - 즉, a:b = 2:3 -> 3*a = b*2 -> a = b*2 / 3
    - 따라서 균형을 이루는 쌍 중 하나만 알아도 다른 쪽이 존재하는지 구할 수 있다.

- 각각 주어진 몸무게 목록은 서로 구분되는 수이다.
    - 따라서 똑같은 몸무게가 여럿 존재할 경우, 가능한 조합의 수는 1부터 해당 몸무개의 개수까지의 합이다.
    - e.g. count(weight of 100) = 3, 가능한 조합의 수 => 3 / (3-1) / 2 = 3개
    - 즉, <100a, 100b>, <100a, 100c>, <100c, 100a>

[풀이]
1. 주어진 몸무게 목록에서 몸무게 별 빈도수를 집계한다.
2. 각 몸무게 별로 다음 연산을 수행한다.
    1. 1:1 비율에서 조건이 성립하는 경우를 계산한다.
        - 1부터 (P1의 개수)까지의 합 => 거듭 제곱 합 공식 적용
    2. 현재 몸무게와 균형을 이룰 수 있는 값이 있는지 조회한다.
        - 2:3 => a*2 / 3
        - 2:4 => a*2 / 4
        - 3:4 => a*3 / 4
        - 값이 존재할 경우, 균형이 성립되며, 이때 해당 값의 개수만큼 쌍을 이룰 수 있기 때문에 다음 연산을 적용한다.
            현재 값 P1에서 균형을 이룰 수 있는 경우의 수
                = (2:3 에서 균형을 이루는 수의 개수) * (P1의 개수)
                  + (2:4 에서 균형을 이루는 수의 개수) * (P1의 개수)
                  + (3:4 에서 균형을 이루는 수의 개수) * (P1의 개수)
"""
from collections import Counter


def solution(weights):
    w_counter = Counter(weights)
    answer = 0

    for weight, count in w_counter.items():
        if count > 0:
            answer += count * (count - 1) // 2
            answer += count * w_counter[weight * 2 / 3]
            answer += count * w_counter[weight * 2 / 4]
            answer += count * w_counter[weight * 3 / 4]

    return answer
