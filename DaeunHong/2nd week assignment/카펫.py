# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def divisor_pairs(n):
    pairs = []
    for i in range (1, n + 1):
        if n % i == 0 and i >= n // i:
            pair = (i, n //i)
            pairs.append(pair)
    return pairs

brown, yellow = map(int, input().split())
square_count = brown + yellow
divisor_list = []
w = 0
h = 0

divisor_list = divisor_pairs(square_count)

for i in range(len(divisor_list)):
    if (divisor_list[i][0] - 2) * (divisor_list[i][1] - 2) == yellow:
        w = divisor_list[i][0]
        h = divisor_list[i][1]

answer = [w, h]

print(answer)

"""
# 근의 공식 풀이 

import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
"""