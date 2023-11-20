"""
LV2. 쿼드압축 후 개수 세기
[https://school.programmers.co.kr/learn/courses/30/lessons/68936]

풀이:
주어진 2차원 배열을 4등분으로 분할하며, 각 나눈 영역에 대해 다음을 검사한다.

- 주어진 영역이 모두 같은 요소로 이루어져 있는지 판별한다.
- 모두 같은 요소인 경우, 해당 요소의 개수를 +1 한다.
- 다른 요소가 존재하는 경우, 다른 요소를 검사한다.

위 과정을 계속 4등분으로 나누어 각 영역의 요소가 1이 될때까지 반복한다.
"""


def solution(arr):
    answer = {0: 0, 1: 0}

    def check(x, y, size):
        return all(arr[x][y] == arr[i][j] for i in range(x, x + size) for j in range(y, y + size))

    def dfs(x, y, size):
        if check(x, y, size):
            answer[arr[x][y]] += 1
            return

        k = size // 2
        dfs(x, y, k)
        dfs(x + k, y, k)
        dfs(x, y + k, k)
        dfs(x + k, y + k, k)

    dfs(0, 0, len(arr))
    return list(answer.values())


t = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1]
]
print(solution(t))
