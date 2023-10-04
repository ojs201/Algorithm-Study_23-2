"""
LV2. 예상 대진표
[https://school.programmers.co.kr/learn/courses/30/lessons/12985]

풀이:
- 문제의 제한 사항에 따르면 문제의 수는 항상 2의 지수 승이므로 항상 포화 이진 트리의 형식을 따름
- 따라서 단말 노드의 자녀(sibling) 수는 항상 2개이며, 부모 노드의 값이 2N일 때 자식 노드는 [N, N+1] 형태임
- 따라서 주어진 입력 A와 B에 대하여 트리의 단말 노드의 시작점이라 가정하고
  두 노드의 값이 서로 같을 때까지 부모 노드 방향으로 이동하는 과정에서 이동 횟수를 세어 이를 반환할 수 있다.
"""


def solution(n, a, b):
    if a == b:
        return 0
    return 1 + solution(n, (a + 1) // 2, (b + 1) // 2)
