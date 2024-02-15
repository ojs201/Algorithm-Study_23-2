#표현식 안에있는 연산자 찾아내고, 순열로 우선순위 리스트를 만든다.
#우선순위 리스트를 돌면서 해당 우선순위로 표현식을 계산한다.

#우선순위로 표현식을 계산하는 로직
#우선순위 : (*, +, -), 표현식 : 100 - 200 * 300 - 500 + 20 라고 할 떄
#계산 전 표현식이 담긴 expressiondq, 특정 연산자 계산이 끝난 expressiondq_next
#1. while(expressiondq) 돌면서
#2. expression = expressiondq.popleft()
#3. expression이 현재 계산해야할 연산자가 아니라면 expressiondq_next에 넣기
#4. expression이 현재 계산해야할 연산자일 경우 expressiondq_next의 마지막에 있는 수와 expressiondq의 앞에 있는 수를 가지고 계산 후 expressiondq_next에 넣기
#5. expressiondq = expressiondq_next
#위 1234과정을 우선순위 : (*, +, -) 다 진행해준다.


import copy
from collections import deque
import itertools

def solution(expression):
    answer = 0
    expressiondq = deque()
    operationSet = set()
    #연산자 종류 확인 & 분리작업
    temp = ""
    for i in expression:
        if(i.isdigit()):
            temp += i
        else:
            operationSet.add(i)
            expressiondq.append(int(temp))
            expressiondq.append(i)
            temp = ""
    expressiondq.append(int(temp))
    #우선순위 순열 구하기 & 해당 우선순위로 계산하기
    prioritys = itertools.permutations(operationSet, len(operationSet))
    for priority in prioritys:
        answer = max(answer, abs(calExpressionWithPriority(priority, expressiondq)))
    return answer

def calExpressionWithPriority(priority, expressiondq):
    expressiondq = copy.deepcopy(expressiondq)
    for operation in priority:
        expressiondq_next = deque()
        while(expressiondq):
            expression = expressiondq.popleft()
            if(expression != operation):
                expressiondq_next.append(expression)
            else:
                expressiondq_next.append(cal(expressiondq_next.pop(), expression, expressiondq.popleft()))
        expressiondq = expressiondq_next
    return expressiondq[0]
    
def cal(num1, operation, num2):
    if(operation == "+"):
        return num1 + num2
    elif(operation == "-"):
        return num1 - num2
    elif(operation == "*"):
        return num1*num2

