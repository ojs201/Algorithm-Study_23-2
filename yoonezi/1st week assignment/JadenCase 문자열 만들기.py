# ====================================================================
# 첫 풀이 -> 런타임 에러 

def solution(s):
    arr = list(s.split(' '))
    answer = []
    for a in arr:
        answer.append(a[0].upper()+a[1:].lower())
    return ' '.join(answer)

# =====================================================================

# 두번째 풀이 -> 성공
# 첫문자 대문자, 나머지는 소문자를 만들 때 capitalize() 사용하자

def solution(s):
    arr = s.split(' ')
    answer = []
    for a in arr:
        answer.append(a.capitalize())        
    return ' '.join(answer)



