# 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

import sys
s = sys.stdin.readline().rstrip()

stack = []

for i in range(len(s)):
    if not stack:
        stack.append(s[i])
    elif stack[-1] == s[i]:
        stack.pop()
    else:
        stack.append(s[i])

if not stack:
    print(1)
else:
    print(0)

