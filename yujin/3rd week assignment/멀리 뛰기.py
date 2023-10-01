def solution(n):
    if n < 3:
        return n
    stairs = [0 for _ in range(n+1)]
    stairs[1] = 1
    stairs[2] = 2
    for i in range(3,n+1):
        stairs[i] = stairs[i-1]+stairs[i-2]
    return stairs[n] % 1234567