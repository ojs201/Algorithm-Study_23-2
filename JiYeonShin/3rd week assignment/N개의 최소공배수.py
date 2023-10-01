def solution(arr):
    answer = 0
    maxOfArr = max(arr)
    while(1):
        answer += maxOfArr 
        for i in arr:
            if(answer % i != 0):
                break
        else:
            break
    return answer