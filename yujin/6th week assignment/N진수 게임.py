def numeral(n, b):
    base = "0123456789ABCDEF"
    s = ''
    if n == 0:
        return '0'
    while n > 0:
        s += base[n % b]
        n //= b
    return s[::-1]

def solution(n, t, m, p):
    answer = ''
    change = ''
    i = 0
    while len(answer) < t:
        change += numeral(i, n)
        i += 1
        if len(change) > m * t:
            break
    for j in range(t):
        answer += change[j * m + p - 1]
    return answer