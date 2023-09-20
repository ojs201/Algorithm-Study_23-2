# 아이디어 : 가장 큰 값 x 가장 작은 값 순으로 더해나가는 값이 최솟값

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i] * B[i]
   
    return answer