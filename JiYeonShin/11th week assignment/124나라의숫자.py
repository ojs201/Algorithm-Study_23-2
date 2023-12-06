# 각 자리수에는 1,2,4 이 3개의 숫자만 올 수 있다.
# 이전에 풀었던 n진법 문제와 비슷하게 3진법처럼 풀 수 있다.
# 단, 원래 n진법에서는 나머지를 그대로 추가했다면 이 경우 나머지를 -> 1,2,4로 바꿔서 추가해준다.

def solution(n):
    answer = ''
    while(n != 0):
        share, remain = divmod(n-1, 3)
        answer = str(2**remain) + answer
        n = share
    return answer