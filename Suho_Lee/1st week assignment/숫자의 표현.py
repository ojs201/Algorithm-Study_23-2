# 첫번째 풀이 : 시간초과
def solution(n):
    
    li = [i for i in range(1, n+1)]
    
    answer_li = []
    answer = 0
    
    for i in range(2, len(li)):
        for j in range(n):
            if sum(li[j:j+i]) == n:
                answer_li.append(li[j:j+i])
    
    for i in answer_li:
        if len(i)!=1:
            answer += 1
    
    return answer +1 

            
# 두번째 풀이 : 리스트로 구현 X
# 1) 연속된 숫자의 합이 n과 같다면 cnt+=1, break하여 다음 시작 숫자로 넘어감
# 2) 연속된 숫자의 합이 n보다 커진다면, break; -> 시간초과를 방지하기 위함.
def solution(num):
    answer = 0
    for x in range(1,num+1):
        sum = 0
        for y in range(x, num+1):
            sum += y
            if sum == num:
                answer += 1
                break
            elif sum > num:
                break

    return answer