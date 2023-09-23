def solution(n):
    arr = [0 for _ in range(100001)]
    arr[0], arr[1] = 0, 1
    answer = 0
    for i in range(2, n+1):
        arr[i] = arr[i-2] + arr[i-1]
    answer = arr[n]%1234567
    return answer