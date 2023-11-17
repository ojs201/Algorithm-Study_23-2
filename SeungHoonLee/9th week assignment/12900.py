"""
LV2. 2 x n 타일링
[https://school.programmers.co.kr/learn/courses/30/lessons/12900]

풀이:
- 다음 점화식을 계산한다.

DP[N] = 가로의 길이가 N일 때 타일을 채우는 방법의 수

DP[1] = 1
DP[2] = 2
DP[3] = DP[1] + DP[2] = 3
DP[4] = DP[2] + DP[3] = 5
DP[5] = DP[3] + DP[4] = 8

=> DP[N] = (DP[N-1] + DP[N-2]) % 1,000,000,007
"""


def solution(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000_007

    return dp[n - 1]
