"""
LV2. 귤 고르기
[https://school.programmers.co.kr/learn/courses/30/lessons/138476]

풀이:
1. 귤을 크기별로 분류한다.
2. 내림차순으로 분류된 귤 개수를 센다.
3-A. 귤의 개수가 'k'개보다 작을 경우:
    - 다음 순서로 넘어간다.
3-B> 귤의 개수가 'k'개 이상일 경우:
    - 현재까지 센 귤들을 포함하는 크기별 분류의 개수를 반환한다.
"""
from collections import Counter


def solution(k, tangerine):
    total = 0
    answer = 0
    count_by_size = Counter(tangerine).values()

    for count in sorted(count_by_size, reverse=True):
        total += count
        answer += 1

        if total >= k:
            break

    return answer
