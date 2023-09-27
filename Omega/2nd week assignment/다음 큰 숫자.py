# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

n = int(input())
nb = bin(n)
k = n

while True:
    k += 1
    if bin(k).count('1') == nb.count('1'):
        break

print(k)

"""
# 제출용 코드
def solution(n):
    nb = bin(n)
    k = n
    
    while True:
        k += 1
        if bin(k).count('1') == nb.count('1'):
            break
            
    return k
"""