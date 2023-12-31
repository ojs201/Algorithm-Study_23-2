# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False

    return cnt == 0