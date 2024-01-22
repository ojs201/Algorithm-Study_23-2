"""
LV2. 행렬 테두리 회전하기
[https://school.programmers.co.kr/learn/courses/30/lessons/77485]

행렬 회전 시 주의할 점:
- 행렬 회전의 시작 위치는 무관
- 단, 시작 위치 이후 순서는 이전 방향 이동 후 발생한 중복값을 보안하는 방향으로 가야한다.
    - 예를 들어 처음 시작 위치를 왼 -> 오 방향으로 정하면:
        - [8, 9, 10] -> [8, 8, 9]
        - 이때 발생하는 문제점은 8이 중복되고, 10이 소실된다는 것
        - 따라서 중복 문제를 해결하기 위해 다음 위치는 [아래 -> 위] 방향이 되어야 하며,
        - 소실된 10은 테두리 회전 이후 회전시킨 상태에 맞는 위치에 적용시켜 주어야 한다.

    - 즉, [왼 -> 오] 방향으로 회전을 시작했다면:
        1. [왼 -> 오]
        2. [아래 -> 위]
        3. [왼 <- 오]
        4. [위 -> 아래]
        5. 처음 소실된 값 복원
    - 위와 같이 각 방향에 따라 이동시켰을 대 발생하는 중복 값을 보안하는 방향을 선택해야 한다.
"""


def rotate(matrix, query):
    """
    주어진 회전 좌표에 따라 행렬의 테두리를 회전시킨 후
    회전 시킨 행렬의 요소 중 최소값을 반환한다.
    """
    query = [pos - 1 for pos in query]
    x1, y1, x2, y2 = query

    tmp = matrix[x1][y1]
    min_val = tmp

    # 아래 -> 위
    for i in range(x1, x2):
        matrix[i][y1] = matrix[i + 1][y1]
        min_val = min(min_val, matrix[i + 1][y1])

    # 왼 <- 오
    for i in range(y1, y2):
        matrix[x2][i] = matrix[x2][i + 1]
        min_val = min(min_val, matrix[x2][i + 1])

    # 아래 <- 위
    for i in range(x2, x1, -1):
        matrix[i][y2] = matrix[i - 1][y2]
        min_val = min(min_val, matrix[i - 1][y2])

    # 왼 -> 오
    for i in range(y2, y1, -1):
        matrix[x1][i] = matrix[x1][i - 1]
        min_val = min(min_val, matrix[x1][i - 1])

    # 행렬 회전 후 처음 위치가 소실되기 때문에 시작 값 복원 필요
    matrix[x1][y1 + 1] = tmp
    return min_val


def solution(rows, columns, queries):
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    return [rotate(matrix, query) for query in queries]


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
