def solution(n):
    arr = [1,2]
    for i in range(2,n):
        arr.append((arr[i-2]+arr[i-1]) % 1000000007)  # 시간초과 방지
    return arr[-1]