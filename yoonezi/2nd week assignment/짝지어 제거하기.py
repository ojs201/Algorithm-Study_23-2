def solution(s):
    
    #1차 : 반복문으로 안될까? > 실패
    # tmp = []
    # print(len(s))
    
    # for i in range(len(s)-1): # 문자열을 돌면서
    #     if s[i] == s[i+1]: # 현재 문자와 다음 문자가 같으면
    #         tmp = s[:i] + s[i+2:]
    #         print(tmp)
               
    # answer = -1
    # return answer
    
    #2차 : 중복을 없애주는 함수 만들어볼까? > 실패
    
    #     tmp = []
    
#     def overlap(a):
#         print(a)
#         tmp = s[:a] + s[a:]
#         print(tmp)
        
#         return tmp
        
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             overlap(i)

#     print(tmp)
            
    

# 3차 : 그래 걍 스택쓰자 > 성공
  
    stack = []
    for i in s:
        if len(stack) < 1:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
            # print(stack)
        else:
            stack.append(i)
            # print(stack)
    if stack == []:
        answer = 1
        # return 1
    else:
        answer = 0
        # return 0
    return answer
def solution(s):
    # tmp = []
    # print(len(s))
    
    # for i in range(len(s)-1): # 문자열을 돌면서
    #     if s[i] == s[i+1]: # 현재 문자와 다음 문자가 같으면
    #         tmp = s[:i] + s[i+2:]
    #         print(tmp)
               
    # answer = -1
    # return answer
    
    
    # stack = []
    # for i in range(len(s)-1):
    #     stack.append(s[i])
    #     print(stack)
        # if s[i] == s[i+1]:
        #     print(s[i], s[i+1])
    
    # for i in range(len(s)-1):
    #     if s[i] == s[i+1]:
    #         stack.pop()
    #         print(stack)
    #         # print(i, s[i], s[i+1])
    
    stack = []
    for i in s:
        if len(stack) < 1:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
            # print(stack)
        else:
            stack.append(i)
            # print(stack)
    if stack == []:
        answer = 1
        # return 1
    else:
        answer = 0
        # return 0
    return answer
    
            
            
        
    # for i in range(len(s)):
        # stack.append(s[i])
        # if len(stack) > 1:
        #     # print(i)
        #     if stack[i-1] == stack[i]:
        #         # print(stack[i-1], stack[i])
        #         # print(stack)
        #         stack.pop()
        #         print(stack)
        #     else:
        #         stack.append(s[i])
        #         print(stack)
                
                # stack.pop()
                
    
#     tmp = []
    
#     def overlap(a):
#         print(a)
#         tmp = s[:a] + s[a:]
#         print(tmp)
        
#         return tmp
        
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             overlap(i)

#     print(tmp)
            
    


# s = "baabaa"