# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

"""
n = int(input())
cnt = 0
k = int((n / 2) + 1)

for i in range(1, k):
    for j in range(i + 1, k):
        i += j
        if i > n:
            break
        elif i == n:
            cnt += 1
            break
print(cnt)
"""


def solution(n):
    cnt = 0
    k = int((n // 2) + 1)

    for i in range(1, k):
        for j in range(i + 1, n):
            i += j
            
            if i > n:
                break
            elif i == n:
                cnt += 1
                break
    
    return cnt + 1