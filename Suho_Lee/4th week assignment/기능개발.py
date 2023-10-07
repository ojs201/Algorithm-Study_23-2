# 나의 풀이 -> 100/100
# 스택/큐 문제인데, 스택 큐로 풀지 않고, 단순 구현으로 풀었음.

def solution(progresses, speeds):
    li = []
    result = []
    cnt = 1
    
    # 1. 각 작업이 100이 될 때 까지 걸리는 일수를 따로 리스트로 만들어줌.
    for i,j in zip(progresses, speeds):
        num = (100-i)//j if (100-i)%j==0 else ((100-i)//j) + 1
        li.append(num)

    # print(li) -> testing code
    
    
    # 2. 최대값 저장 변수
    max = li[0]
    
    
    # 3. 방법은 max와 다음값을 비교하여 max가 크거나 같다면 cnt를 증가시키고 다음으로 넘어감
    # max가 작다면 max값을 바꿔주고, result 리스트에 cnt를 추가해줌.
    for i in range(1, len(li)):        
        if max >= li[i]:
            cnt += 1 
            continue
        else:
            max = li[i]
            result.append(cnt)
            cnt = 1
    
    # 4. 마지막 cnt는 for문을 len(li)-1로 설정했기에 포함되지 않기에 따로 추가해줌.
    result.append(cnt)
      
    return result