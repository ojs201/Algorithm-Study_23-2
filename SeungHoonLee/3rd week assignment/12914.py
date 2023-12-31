""""
LV2. 멀리 뛰기
[https://school.programmers.co.kr/learn/courses/30/lessons/12914]

풀이:
- 칸의 수 N이 주어졌을 때 방법의 수를 직접 계산해 보았다.

N = 1: -> 1
1
---
N = 2: -> 2
(1 + 1)
2
---
N = 3: -> 3
(1 + 1 + 1)
(2 + 1)
(1 + 2)
---
N = 4: -> 5
(1 + 1 + 1 + 1)
(2 + 1 + 1)
(1 + 2 + 1)
(1 + 1 + 2)
(2 + 2)
---
N = 5: -> 8
(1 + 1 + 1 + 1 + 1)
(2 + 1 + 1 + 1)
(1 + 2 + 1 + 1)
(1 + 1 + 2 + 1)
(2 + 2 + 1)
(1 + 1 + 1 + 2)
(2 + 1 + 2)
(1 + 2 + 2)
...

위와 같이 칸 수 N이 주어 졌을 때, 방법 sol(N)은 아래와 같다.

| N   | sol(N) |
| --- | ------ |
| 1   | 1      |
| 2   | 2      |
| 3   | 3      |
| 4   | 5      |
| 5   | 8      |

따라서 sol(N)은 다음과 같이 정리할 수 있다:

sol(N) = sol(N-1) + sol(N-2) [단, N > 2]
"""


def solution(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a % 1234567
