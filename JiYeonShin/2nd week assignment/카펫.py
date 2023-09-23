def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if(yellow%i != 0):
            continue
        width = yellow//i
        high = i
        if(width*2 + high*2 + 4 == brown):
            answer.extend([width+2, high+2])
            break
    return answer