# 피보나치 > 재귀함수 ? 더 단순하게 짜보고싶다.. 반복문으로 해보자
def solution(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    
    answer = fibo[-1] % 1234567
    return answer