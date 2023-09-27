# 나의 코드
def solution(n):
    battery_usage = 0
    
    while n:
        if n%2==0:
            n//=2
        else:
            n-=1
            battery_usage += 1
    
    return battery_usage


#################################################################################


# 다른 사람의 코드 -> 멋있는 코드다..!
def solution(N):
    answer = 0
    while N > 0:
        answer += N % 2
        N //= 2
    return answer