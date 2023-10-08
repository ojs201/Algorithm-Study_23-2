"""
LV2. H-Index
[https://school.programmers.co.kr/learn/courses/30/lessons/42747]

H-Index의 조건:
발표한 논문 n편 중 아래 2가지 조건을 만족하는 값 중 최댓값이다.

1. h번 이상 인용된 논문이 h편 이상이다.
2. 나머지 인용된 논문이 h번 이하이다.

풀이:
1. 논문 인용 횟수를 내림차 순으로 정렬한다.
  - 내림차순으로 정렬했을 때 인덱스 번호 `h`는 '인용된 논문의 횟수'로 사용된다.

2. h에 대해 0부터 시작해서 아래 조건에 따라 연산을 적용한다.

  2.1 h와 인용횟수(citation)를 비교한다.
    A. h >= citation:
      - 지금까지 센 인용된 논문의 횟수(h)가 현재 인용 횟수보다 크거나 같으므로
        h가 H-Index 조건에 만족하는 최대 값이 된다.
    B. h < citation:
      - 인용된 논문의 횟수가 H-Index에 만족하지 않으므로 넘어간다.

    e.g.
    [0, 0, 0, 0]
      -> 전체 논민 인용 횟수가 모두 0이므로 H-Index는 0이다.
    e.g.
    [1, 2, 3, 4, 5]
      -> 논문 인용 횟수를 내림차순 정렬한다.
    [5, 4, 3, 2, 1]
      -> 인용된 논문의 횟수(h)를 각 논문의 인용 횟수(citation)와 비교한다.
      -> 인용된 논문의 횟수 개수가 3일 때 3번 이상 인용된 논문의 개수가 3편 이상이고,
         나머지 인용된 논문 횟수 또한 3편 이하이므로 3이 H-Index의 최대값이 된다.

    | h   | citation |
    | --- | -------- |
    | 0   | 5        |
    | 1   | 4        |
    | 2   | 3        |
    | 3   | 2        |
    | 4   | 1        |

3. 정해진 H-Index에 따라 아래를 적용한다.

  A. H-Index 값이 정해진 경우:
    - 그대로 반환한다.

  B. H-Index 값이 정해지지 않은 경우:
    - 위 로직에 대한 반례로 다음과 같은 경우가 있다.
      e.g.
      [1] => 1
      [2, 2] => 2
      [3, 3, 3] => 3

    - 이는 H-Index 값이 논문의 개수와 동일한 경우로,
    - 위 로직에서 사용한 `h`는 인덱스 값이므로 위 경우를 해결할 수 없다.
    - 따라서 이런 경우는 인용횟수 리스트의 길이를 반환한다.
"""


def solution(citations):
    citations.sort(reverse=True)
    return next((h for h, citation in enumerate(citations) if h >= citation), len(citations))


def solution2(citations):
    h = 0
    for citation in sorted(citations, reverse=True):
        if h >= citation:
            break
        h += 1
    return h
