# sort 함수를 사용해서 A를 오름차순, B를 내림차순으로 정렬
# 각 배열에서 최댓값과 최솟값을 곱해서 누적하면 최솟값을 얻을 수 있음(한 번 사용한 숫자는 빼기)

# ====================================================================
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[i]*B[-1-i]
    return answer


# ====================================================================
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer