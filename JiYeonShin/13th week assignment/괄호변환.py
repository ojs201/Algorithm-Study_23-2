#그대로 구현만 해주면 되는 문제.

#과정이 길어서 올바른 괄호열인지 확인하는 함수와, 
#괄호문자열을 모두 뒤집는 함수로 따로 빼주었다.


def solution(p):
    answer = ''
    if(len(p) == 0): #빈 문자열인 경우
        return p
    cnt = 0
    u , v = "", ""
    for i, bracket in enumerate(p): #두 "균형잡힌 괄호 문자열"로 분리
        if(bracket == "("):
            cnt += 1
        else:
            cnt -=1
        if(cnt == 0):
            u = p[:i+1]
            v = p[i+1:]
            break
    if(isCollectBrackets(u)): #u가 올바른 괄호 문자열이라면
        return u + solution(v)
    else: #u가 올바른 괄호 문자열이 아니라면
        return "(" + solution(v) + ")" + reverseBrackets(u[1:-1])
        
def reverseBrackets(brankets):
    reverseBrackets = ""
    for b in brankets:
        if(b == "("):
            reverseBrackets += ")"
        else:
            reverseBrackets += "("
    return reverseBrackets

        
def isCollectBrackets(u):
    cnt = 0
    for bracket in u:
        if(bracket == "("):
            cnt += 1
        else:
            if(cnt != 0):
                cnt -= 1
            else:
                return False
    if(cnt == 0):
        return True
    else:
        return False
    
                

