#문제설명 : 합이 k인 수열, 길이가 가장 짧으면서 시작 인덱스가 작아야함!

#sequence길이만큼 순회하면서
    #1. dq에 담기, sum(현재 수 합)에 값 더하기
    #2. sum이 k보다 작거나 같아질 때까지 dq의 제일 앞에 있는 수를 pop, 이때 sum에서 값 빼주기 
    #3. sum = k일 경우, 정답 후보이므로 answer에 (길이, 시작인덱스, 끝인덱스) 추가
#길이가 작은 순, 시작인덱스가 작은 순으로 정렬 후 0번째 인덱스에 있는 값 return

from collections import deque

def solution(sequence, k):
    answer = []
    dq = deque()
    sum = 0
    for i in range(len(sequence)):
        dq.append(sequence[i])
        sum += sequence[i]
        while(sum > k):
            sum -= dq.popleft()
        if(sum == k):
            answer.append((len(dq), i-len(dq)+1, i))
    answer.sort(key = lambda x : (x[0], x[1]))
    return [answer[0][1], answer[0][2]]

