def solution(n):
    s = ''
    while n > 0:
        if n % 3 == 0:
            s += '4'
            n = n//3 - 1
        else:
            s += str(n%3)
            n //= 3
            
    return s[::-1]