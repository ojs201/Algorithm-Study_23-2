# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter
def solution(k, tangerine):
    answer = 0
    C = Counter(tangerine)
    sorted_c = list(C.items())
    sorted_c.sort(key=lambda x:x[1])
    cnt = 0
    while cnt < k:
        answer += 1
        cnt += sorted_c.pop()[1]
    return answer