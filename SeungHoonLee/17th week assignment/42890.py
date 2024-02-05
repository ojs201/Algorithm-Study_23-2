"""
LV2. 후보키
[https://school.programmers.co.kr/learn/courses/30/lessons/42890]

풀이:
1. 후보키로 사용할 수 있는 모든 조합의 경우의 수를 구한다.
2. 각 후보키 조합에 대해 아래 연산을 수행한다.
    2. 후보키에 대한 유일성을 검증한다.
        2-1. 후보키의 요소로 테이블의 튜플(tuple, 테이블의 행)을 산출한다.
        2-2. 산출된 전체 행이 중복되지 않았는지 검사한다.
    3. 후보키에 대한 최소성을 검증한다.
        3-1. 다른 후보키 조합에서 현재 후보키 요소를 가지는 조합들을 제외한다.
    4. 유일성과 최소성의 검증이 완료된 후보키에 대해 경우의 수를 센다.
3. 후보키 경우의 수를 반환한다.
"""
from itertools import combinations


def solution(relation):
    n = len(relation[0])
    rows = len(relation)

    candidates = []
    for r in range(1, n + 1):
        candidates.extend(combinations(range(n), r))

    answer = 0

    while candidates:
        index = list(map(int, candidates.pop(0)))
        mapped = [tuple(map(lambda i: v[i], index)) for v in relation]

        if len(set(mapped)) != rows:
            continue

        i = 0
        while i < len(candidates):
            if all(num in candidates[i] for num in index):
                candidates.pop(i)
                i -= 1
            i += 1

        answer += 1

    return answer
