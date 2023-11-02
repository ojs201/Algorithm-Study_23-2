def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def to_k(n, k):
    lst = []
    while n > 0:
        r = n % k
        lst.append(str(r))
        n = n // k
    lst.reverse()
    return ''.join(lst)


def solution(n, k):
    answer = 0
    k_num = to_k(n, k)
    for n in k_num.split('0'):
        if n == "":
            continue
        if is_prime(int(n)):
            answer += 1
    return answer