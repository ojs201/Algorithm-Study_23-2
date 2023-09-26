#dp이용 풀이 => 전 칸에서 +1하기, //2칸 에서 순간이동하기 =>O(N) 시간초과
# def solution(n):
#     dp = [0 for i in range(n+1)]
#     for i in range(1, n+1):
#         dp[i] = dp[i-1] + 1
#         if(i%2 == 0):
#             dp[i] = min(dp[i], dp[i//2])
#     return dp[n]


#O(logN)
#5000 -> 2500 -> 1250 -> 625 -> (-1) => 624 -> 312 -> 156 -> 78 -> 39 -> (-1) -> 38 -> 19 -> (-1) -> 18 -> 9 -> (-1) => 8 -> 4 -> 2 -> 1 -> (-1) 
def solution(n):
    ans = 0
    while(n != 0):
        if(n%2 == 0):
            n = n//2
        else:
            ans += 1
            n -= 1
    return ans
