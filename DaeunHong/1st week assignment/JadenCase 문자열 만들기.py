# JadenCae 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    s_list = s.split(" ")
    result = list(map(str.capitalize, s_list))
    answer = ' '.join(result)
    return answer

"""
import sys

data = str(sys.stdin.readline().rstrip())

data_list = data.split(" ")
result = list(map(str.capitalize, data_list))

print(' '.join(result))
"""
