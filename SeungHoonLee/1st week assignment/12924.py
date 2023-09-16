"""
LV2. 숫자의 표현
[https://school.programmers.co.kr/learn/courses/30/lessons/12924]

시간 복잡도: O(N^2)

풀이:
- 숫자 N에 대해 1부터 K(= N의 절반 + 1)까지 다음 과정을 반복한다:
    - 숫자 i (1 <= i <= K) 부터 K까지의 수를 덧셈한다.
    - 더해진 수 T가 숫자 N보다 크거나 같을 경우 덧셈을 종료한다.
    - T가 N과 같을 경우 카운트 C를 하나 증가 시키고, 아닐 경우 종료한다.
    - 숫자 i를 +1 증가 시킨다.
- 카운터 C를 반환한다.

예외 케이스:
- 숫자 1의 경우 K를 구할 때 1보다 큰 수가 반화됨
- 따라서 숫자 N이 2보다 작을 경우 숫자 N을 그대로 반환
"""


def solution(n):
    if n < 2:
        return n

    k = (n + 1) // 2 + 1
    answer = 0

    for i in range(1, k):
        total = 0

        for j in range(i, k):
            total += j

            if total >= n:
                break

        answer = answer + 1 if total == n else answer
    return answer + 1
