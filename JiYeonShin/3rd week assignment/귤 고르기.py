from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    dict = defaultdict(int)
    for i in tangerine:
        dict[i] += 1
    TangerineInfo = sorted(dict.items(), key = lambda x : -x[1])
    for j in range(len(TangerineInfo)):
        k -= TangerineInfo[j][1]
        if(k <= 0): #귤 다 담음
            answer = j+1
            break
    return answer

#{귤의 종류 : 개수} 만들고 제일 개수가 많은 귤 종류 부터 채워나간다.