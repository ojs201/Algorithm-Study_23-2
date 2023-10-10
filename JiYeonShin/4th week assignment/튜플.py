from collections import defaultdict
from collections import deque

def solution(s):
    answer = []
    dict = defaultdict(int)
    s = s.replace("{", "")
    s = s.replace("}", "")
    for i in s.split(","):
        dict[i] += 1
            
    sorteddict = sorted(dict.items(), key = lambda x : -x[1])
    for i in sorteddict:
        answer.append(int(i[0]))
    return answer