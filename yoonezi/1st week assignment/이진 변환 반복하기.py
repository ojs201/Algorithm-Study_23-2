# # 구해야 하는 것 : 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수

def solution(s):
    zerocnt, cnt = 0, 0
    while s != '1': #0이 없을 때까지 반복
        cnt += 1 # 변환 횟수 +1
        num = s.count('1')
        zerocnt += len(s) - num
        s = bin(num)[2:] #이진변환 해주고, ob 제외
    
    return [cnt, zerocnt]

## 이진 변환 bin()에 대해서 배운 문제
## 0인지 아닌지 조건문으로 달아서 할까 하다가, 더 쉬운 방법있지 않을까 고심
