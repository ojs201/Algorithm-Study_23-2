# ====================================================================
# 시간초과
def solution(s):
    s = s.replace("()","")
    if s == "()":
        answer = True
    else:
        answer = False
    return answer

# ====================================================================
def solution(s):
    answer = 0
    for i in s:
        if i == "(":
            answer+=1
        #elif i == ")":
        else:
            if answer>0:
                answer-=1
            else:
                return False
    return answer == 0