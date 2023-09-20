def solution(A,B):
    answer = 0

    new_A = sorted(A)
    new_B = sorted(B, reverse=True)
    
    # zip함수로 두 리스트 묶기 -> 각 원소를 a,b로 받을 수 있음.
    for a,b in zip(new_A, new_B):
        answer += (a*b)

    return answer