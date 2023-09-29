# gcd 이용하기
# 모든 배열을 돌면서 
# a = [0], [1] 의 최소 공배수 -> a + [2]의 최소 공배수 .. 순으로
from math import gcd

def solution(arr):
    
    answer = arr[0]    
    for a in arr:
        answer = answer * a // gcd(answer, a)
    
    return answer