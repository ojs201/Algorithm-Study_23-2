from collections import deque

def solution(order):
    answer = 0
    mainContainer = deque([i+1 for i in range(len(order))])
    secondContainer = deque()
    for i in order:
        if(mainContainer and mainContainer[0]<=i): #찾고자 하는 박스가 컨테이너에 있음
            while(mainContainer and mainContainer[0] != i):
                secondContainer.append(mainContainer.popleft())
            mainContainer.popleft()
            answer += 1
        else: #보조컨테이너에서 찾기
            if(secondContainer[-1] == i):
                secondContainer.pop()
                answer += 1
            else:
                break
    return answer

# 현재 실어야 하는 상자 = i
# 일단 컨테이너를 먼저 봐
# if 컨테이너의 제일 앞에 있는 수가 i보다 작다면 상자 찾을 때 까지 보조컨테이너에 넣기
# else 보조 컨테이너에서 찾기