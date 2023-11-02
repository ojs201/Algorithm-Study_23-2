from collections import deque

def solution(priorities, location):
    answer = [] 
    queue = deque((idx, priority) for idx, priority in enumerate(priorities))
    while queue:
        process = queue.popleft()
        if any(process[1]<q[1] for q in queue):
            queue.append(process)
        else:
            answer.append(process)
            
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1