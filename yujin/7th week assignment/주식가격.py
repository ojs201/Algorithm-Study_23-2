from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        current_price = queue.popleft()
        count = 0
        
        for price in queue:
            count += 1
            if current_price > price :
                break
        answer.append(count)
    return answer