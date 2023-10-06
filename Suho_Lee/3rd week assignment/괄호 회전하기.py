# 나의 풀이
# isStack() 함수 -> 스택 구현 부분 참고


from collections import deque

def solution(s):
    cnt = 0
    
    # 덱으로 구현 (편리함 때문)
    stack = deque(s)
    
    for i in range(len(s)):
        
        # 맨 왼쪽에 원소를 맨 뒤에 붙이기
        stack.append(stack.popleft())
        
        # 1칸씩 회전된 스택이 '올바른 괄호 문자열'인지 확인하는 함수 적용하기
        if isStack(stack):
            cnt += 1
    
    return cnt
        
    
def isStack(stack):
    
    tmp = []
    
    for char in stack:
        if char in ['(', '{', '[']:
            tmp.append(char)
        elif char in [')', '}', ']']:
            #만약 스택 tmp가 비어있는데 닫는 괄호가 나온다면, 이는 유효한 괄호 짝이 아니므로 False
            if not tmp:
                return False
            
            # 현재 닫는 괄호와 스택의 맨 위 괄호를 비교 후 짝이 아니면 False 반환
            top = tmp.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False
    
    # 스택이 비었는지 확인
    # 비어있다면 True 아니면 False
    return not tmp