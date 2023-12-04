"""
LV2. 소수 찾기
[https://school.programmers.co.kr/learn/courses/30/lessons/42839]

풀이:
1. dfs를 이용해 순열의 조합을 구한다.
    - 이때 같은 위치에 존재하는 원소는 중복하여 포함되지 않도록 한다.
2. 각 조합의 숫자가 소수인지 판별한다.
"""


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    unique_numbers = set()
    n = len(numbers)
    visited = [False] * n

    def dfs(total, idx):
        if total != "":
            num = int(total)

            if is_prime(num):
                unique_numbers.add(num)

            if idx == n:
                return

        for i, ch in enumerate(numbers):
            if not visited[i]:
                visited[i] = True
                dfs(total + ch, idx + 1)
                visited[i] = False

    dfs("", 0)
    return len(unique_numbers)
