# 스택 안쓰고 풀 수 있지 않을까? 했다가 대차게 실패한 풀이

# def solution(s):
#     openP = 0
#     closeP = 0
#     answer = True
    
#     for i in range(len(s)):
#         if s[i] == "(":
#             openP += 1
#         else:
#             closeP += 1
            
#     if openP == closeP:
#         answer = True
#     else:
#         answer = False
        
#     if s[0] == ")":
#         answer = False

#     return answer

# ========================================


def solution(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    
    # print(stack == [])
    return stack == []

 