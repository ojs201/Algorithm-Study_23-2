"""
LV2. 의상
[https://school.programmers.co.kr/learn/courses/30/lessons/42578]

시도 방법:
- 다음과 같이 여러 테스트 케이스를 직접 작성해봄.

e.g. clothes = [A: 3]
  - f(clothes) = 3

e.g. clothes = [A: 2, B: 2]
  - f(clothes) = 2 + 2 + (2*2) = 4

e.g. clothes = [A: 3, B: 1]
  - f(clothes) = 3 + 1 + (3*1) = 4

e.g. clothes = [A: 3, B: 1, C: 1]
  - f(clothes) = 3 + 1 + 1 + (3*1) + (1*1) + (1*3) + (3*1*1) = 15
...

- 각 의상의 종류 별로 i개 만큼 고른 경우의 수를 모두 더한 결과가 정답이 된다.
- 위 케이스들에 대한 일반화를 진행하면 아래와 같다.

e.g. clothes = [A: 3]
  - f(clothes) = A

e.g. clothes = [A: 2, B: 2]
  - f(clothes) = A + B + (A*B)

e.g. clothes = [A: 3, B: 1]
  - f(clothes) = A + B + (A*B)

e.g. clothes = [A: 3, B: 1, C: 1]
  - f(clothes) = A + B + C + (A*B) + (B*C) + (C*A) + (A*B*C) = 15

- 위와 같이 식을 정리해보면 의상의 종류 개수에 따라 일반화 된 식으로 검출되는 것을 확인할 수 있음.
- 이때 위 식들을 다항식의 곱셉 공식을 이용하면 아래와 같이 정리할 수 있다.

e.g. clothes = [A, B]
  - f(clothes) = A + B + (A*B)
  - f(clothes) = A + B + (A*B) + 1 - 1
  - f(clothes) = ((A*B) + A + B + 1) - 1
  - f(clothes) = (A+1)(B+1) - 1

=> 즉 의상의 종류가 2개일 때(A,B), f(clothes) = (A+1)(B+1) - 1

e.g. clothes = [A, B, C]
  - f(clothes) = A + B + C + (A*B) + (B*C) + (C*A) + (A*B*C)
  - f(clothes) = (A + B + C)*1^2 + ((A*B) + (B*C) + (C*A))*1 + (A*B*C) + 1 - 1
  - f(clothes) = (A+1)(B+1)(C+1) - 1

=> 즉 의상의 종류가 3개일 때(A,B,C), f(clothes) = (A+1)(B+1)(C+1) - 1

정리:
- 의상을 clothes 라 하고, 의상의 종류가 N개일 때(A,B,...,N)
- 서로 다른 옷 조합의 개수는 f(clothes) = (A+1)(B+1)...(N+1) - 1 이다.

풀이:
- 의상의 종류 별 개수를 집계한다.
- 의상의 종류의 개수에 따라 위 공식을 적용한다.
"""
from functools import reduce


def solution(clothes):
    d = {}
    for cloth, category in clothes:
        d[category] = d.get(category, 0) + 1
    return reduce(lambda x, y: x * (y + 1), d.values(), 1) - 1
