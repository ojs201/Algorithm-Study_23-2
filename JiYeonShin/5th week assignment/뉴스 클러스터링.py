from collections import deque
from collections import defaultdict

def splitToTwoChar(str):
    result = defaultdict(int)
    dq = deque()
    for c in str:
        if(not c.isalpha()):
            if(dq):
                dq.popleft()
            continue
        dq.append(c)
        if(len(dq) == 2):
            result["".join(dq)] += 1
            dq.popleft()
    return result

def solution(str1, str2):
    answer = 0
    #두 글자씩 끊어서 다중집합 만들기
    str1dict = splitToTwoChar(str1.upper())
    str2dict = splitToTwoChar(str2.upper())
    #교집합 수 구하기
    intersection = 0
    for c in str1dict:
        intersection += min(str1dict[c], str2dict[c])
    #합집합 수 구하기
    union = 0
    for c in str1dict:
        union += max(str1dict[c], str2dict[c])
        str1dict[c], str2dict[c] = 0, 0
    for c in str2dict:
        union += max(str1dict[c], str2dict[c])
    if(union == 0):
        return 65536
    return int(intersection/union*65536)


