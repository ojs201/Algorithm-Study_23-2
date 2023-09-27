# stack 자료구조 이용하여 풀이

# <풀이설명>
# 맨처음 스택이 비어있거나, 스택 마지막원소와 현재 집어넣으려는 원소가 같지 않다면 -> 스택에 추가
# 스택 마지막원소와 현재 집어넣으려는 원소가 같다면 -> 스택 pop()
# 결과적으로 스택이 비어있으면 짝지어 제거 성공적으로 수행된 것!!

def solution(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack)==0 or stack[-1] != s[i]:
            stack.append(s[i])
        else: # stack[-1] == s[i]
            stack.pop()

    return 1 if len(stack)==0 else 0