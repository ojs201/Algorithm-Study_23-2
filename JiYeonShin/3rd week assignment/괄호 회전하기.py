import copy
from collections import deque

#꺼냈을 떄 열린 괄호면 그냥 temp에 푸시
#꺼냈을 때 닫힌 괄호면 temp의 -1이 맞는 짝일 경우 temp pop
#닫힌 괄호 인데 맞는 짝이 없다? 올바르지 않은 괄호열
def isRightString(dq):
    temp = deque()
    brankets = copy.deepcopy(dq)
    while(brankets):
        bracket = brankets.popleft()
        if(bracket == "(" or bracket == "[" or bracket == "{"): #여는 괄호
            temp.append(bracket)
        else: #닫는 괄호
            if(not temp):
                return 0
            elif((temp[-1] == "(" and bracket == ")") 
            or (temp[-1] == "[" and bracket == "]") 
            or (temp[-1] == "{" and bracket == "}")):
                temp.pop()
            else:
                return 0
    if(temp):
        return 0
    else:
        return 1
                
def solution(s):
    answer = 0
    dq = deque(s)
    answer += isRightString(dq)
    for _ in range(len(s)-1):
        dq.rotate(1)
        answer += isRightString(dq)
    return answer