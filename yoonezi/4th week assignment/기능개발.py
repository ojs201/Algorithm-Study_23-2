#  만약 "입출력 순서"에 대한 언급이 있다면 stack , queue -> pop 
 

def solution(progresses, speeds):
    answer = []
    day = 0 
    count = 0  
    while len(progresses)> 0: # progresses가 비어있기 전까지 반복
        if (progresses[0] + day*speeds[0]) >= 100: # 만약, (progressed[0]에 진행된 날짜와 속도 ) 값이 100보다 크거나 같다면
            progresses.pop(0) #progresses[0] 꺼내주고
            speeds.pop(0) # 해당 스피드값도 꺼내주고
            count += 1 # 카운트 증가
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer

