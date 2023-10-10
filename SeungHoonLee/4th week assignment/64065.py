"""
LV2. 튜플
[https://school.programmers.co.kr/learn/courses/30/lessons/64065]

풀이:
1. 주어진 문자열을 튜플 단위로 파싱한다.
2. 튜플의 길이를 기준으로 오름차 순으로 정렬한다.
3. 튜플 원소에 따라 아래를 진행한다.
  A. 이전에 나온 원소인 경우:
    - 무시한다.
  B. 처음 나온 원소인 경우:
    - 튜플 집합에 추가한다.
4. 튜플 집합을 반환한다.

풀이2:
문제에서 주어진 튜플의 특징 상 숫자를 기준으로 가장 많이 나온 숫자부터 내림차순으로
배치된 것이 튜플 집합임을 이용한다.
"""
import re
from collections import Counter


def solution(s):
    s = s[2:-2].split('},{')
    answer = []

    for tuple_str in sorted(s, key=len):
        for el in map(int, tuple_str.split(',')):
            if el not in answer:
                answer.append(el)

    return answer


def solution(s):
    c = Counter(re.findall('\d+', s))
    return [int(k) for k, _ in c.most_common()]
