from itertools import combinations        


# 첫번째 풀이 : 12.5/100 -> 시간초과
def solution(n):
    cnt = 1 
    
    for num2 in range(1, n//2+1):
        num1 = (n-2*num2)
        
        if num1 > num2 :
            li = ['0'] * (num1+1)
            cnt += len(list(combinations(li, num2)))
        else:
            li = ['0'] * (num2+1)
            cnt += len(list(combinations(li,num1)))

    return cnt


# 두번째 풀이 : DP + 점화식(피보나치)
def solution(n):
    if n<3:
        return n
    
    dp = [0] * (n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%1234567
    