def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    max_h = citations[0]
    now = 0
    for h in range(max_h, -1, -1):
        for i in range(now, len(citations)):
            if(citations[i] >= h):
                now += 1
            else:
                break
        if(now >= h):
            answer = h
            break
    return answer