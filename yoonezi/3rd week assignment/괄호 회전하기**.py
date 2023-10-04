# 스택이용하면 되지 않을까?
# 1. [](){} 예시를 생각
#   stack.append([)
#   if stack[-1] == [ and s[-1]==]:
#   pop , cnt += 1
#   이런 느낌으로 하면 되지 않을까?

# 2.근데 이걸 왼쪽으로 옮겨야하네 ..?


def solution(s):
    answer = 0
    temp = list(s)
    
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            if len(stack) > 0 :
                if stack[-1] == "(" and temp[j]== ")":
                    stack.pop()
                elif stack[-1] =="[" and temp[j]== "]":
                    stack.pop()
                elif stack[-1] == "{" and temp[j]== "}":
                    stack.pop()  
                else:
                    stack.append(temp[j])
            else:
                stack.append(temp[j])
                
        if len(stack) == 0:
                answer += 1
                
        temp.append(temp.pop(0))

    return answer