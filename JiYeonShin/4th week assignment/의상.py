from collections import defaultdict

def solution(clothes):
    answer = 1
    dict = defaultdict(int)
    for i in clothes:
        dict[i[1]] += 1
    for i in dict.values():
        answer *= (i+1)
    return answer-1