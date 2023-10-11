def solution(s):
    s = s[2:-2].split("},{")
    ele = [list(map(int, x.split(','))) for x in s]
    ele.sort(key=len)
    
    answer = []
    for sublist in ele:
        answer.extend([x for x in sublist if x not in answer])
    
    return answer