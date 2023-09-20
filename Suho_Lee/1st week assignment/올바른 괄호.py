def solution(s):
    stack = []
    
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if len(stack)==0:
                stack.append(i)
            elif len(stack)!=0 and stack[-1] == '(':
                stack.pop()
    
    return False if stack else True
    # return len(st) == 0