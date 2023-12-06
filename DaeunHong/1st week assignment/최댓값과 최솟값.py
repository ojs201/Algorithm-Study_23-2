# 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

import sys
"""
input_data = str(sys.stdin.readline().rstrip())

def solution(s):
    data = s.split()
    mx, mn = int(max(data)), int(min(data))
    if mx < 0 and mx < 0:
        answer = print(str(mx), str(mn))
    else:
        answer = print(str(mn), str(
        mx))
    return answer

solution(initial)
"""

input_data = str(sys.stdin.readline().rstrip())
def solution(s):
    data = list(map(int, s.split()))
    return str(min(data)) + ' ' + str(max(data))

solution(input_data)




