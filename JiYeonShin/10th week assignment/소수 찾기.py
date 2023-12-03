#dfs를 돌아주면서 만들 수 있는 모든 수를 구한다.
#해당 수들을 하나씩 돌면서 소수판별을 해준다.

import math

def solution(numbers):
    answer = 0
    numberset = set() #만들 수 있는 모든 수 저장하는 set
    visit = [False for _ in range(len(numbers))]
    dfs(numbers, [], visit, numberset)
    for n in list(numberset):
        if(isPrimeNumber(n)):
            answer += 1
    return answer

def isPrimeNumber(n):
    if(n == 1 or n == 0):
        return False
    for i in range(2,int(int(n)**0.5)+1):
        if int(n)%i==0:
            return False
    return True
    
def dfs(numbers, numberlist, visit, numberset):
    if(numberlist):
        numberset.add(int("".join(numberlist)))
    for i in range(len(numbers)):
        if(visit[i] == False):
            visit[i] = True
            numberlist.append(numbers[i])
            dfs(numbers, numberlist, visit, numberset)
            visit[i] = False
            numberlist.pop()
    
