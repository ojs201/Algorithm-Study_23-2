"""
LV2. H-Index
[https://school.programmers.co.kr/learn/courses/30/lessons/42747]

H-Index의 조건:
발표한 논문 n편 중 아래 2가지 조건을 만족하는 값 중 최댓값이다.

1. h번 이상 인용된 논문이 h편 이상이다.
2. 나머지 인용된 논문이 h번 이하이다.

풀이:
인덱스 h에 대해 0부터 주어진 논문 인용횟수의 길이만큼 반복하며 조건에 만족하는 최대값을 찾는다.

1. 논문 인용 횟수를 내림차 순으로 정렬한다.
  - 이때 인덱스 번호를 'h', 현재 논문의 인용횟수를 'citation'라 표기

2. h에 대해 0부터 시작해서 아래 조건에 따라 연산을 적용한다.

  2.1 h와 인용횟수(citation)를 비교한다.

    A. h >= citation:
      - 지금까지 인용된 논문의 편수(=h)가 현재 논문의 인용 횟수(=citation)보다 크거나 같으므로
        h가 H-Index 조건에 만족하는 최대 값이 된다.

    B. h < citation:
      - 인용된 논문의 횟수가 H-Index에 만족하지 않으므로 넘어간다.

    e.g.
    [0, 0, 0, 0]
      -> 전체 논문이 인용된 횟수가 모두 0이므로 H-Index는 0이다.
    e.g.
    [1, 2, 3, 4, 5]
      -> 논문 인용 횟수를 내림차순으로 정렬한다.
    [5, 4, 3, 2, 1]
      -> 인용된 논문의 편수(h)를 0부터 시작하여 각 논문의 인용 횟수(citation)와 비교한다.
      -> h가 3일 때 3번 이상 인용된 논문의 개수가 3편 이상이고,
         나머지 인용된 논문 횟수 또한 3편 이하이므로 3이 H-Index의 최대값이 된다.

    | h   | citation |
    | --- | -------- |
    | 0   | 5        |
    | 1   | 4        |
    | 2   | 3        |
    | 3   | 2        |
    | 4   | 1        |

3. 정해진 h에 따라 아래를 적용한다.

  A. h 값이 정해진 경우:
    - 그대로 반환

  B. h 값이 정해지지 않은 경우:
    - 위 로직에 대한 반례로 다음과 같은 경우가 있다.
      e.g.
      [1] => 1
      [2, 2] => 2
      [3, 3, 3] => 3

    - 이는 h 값이 논문 인용횟수 리스트의 길이와 동일한 경우로, `h`는 인덱스 값이므로 위 경우를 해결할 수 없다.
    - 따라서 이런 경우는 리스트의 길이를 반환한다.
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
