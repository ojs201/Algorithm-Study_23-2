# 피보나치느낌으로 a3 = a1 + a2, a4 = a2+ a3

def solution(n):
    fibo = [1, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    answer = fibo[-1] % 1234567
    
    return answer