def solution(n):
    dp = [1, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]%1234567

# 해당 칸으로 갈 수 있는 경우
# 1) 전칸에서 +1칸
# 2) 전전칸에서 +2칸