def solution(n):
    battery = 0
    while n>0:
        if n%2 == 0:
            n//=2
        else:
            battery += 1
            n -= 1
    return battery