# ==============================================================================
# 테스트 케이스 16에서 실패
# h번 이상 인용되어야 하기 때문에 h의 최댓값은 citations의 개수 
def solution(citations):
    n = len(citations)
    while n > 0:
        cnt = 0
        for j in citations:
            if n <= j:
                cnt+=1
        if cnt == n:
            return cnt
        else:
            n -= 1

# ==============================================================================
def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n, 0, -1):
        cnt = 0
        for citation in citations:
            if citation >= i:
                cnt += 1
        if cnt >= i:
            return i
    return 0