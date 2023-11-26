def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

from itertools import permutations
def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    pm = []
    for i in range(1,len(numbers)+1):
        pm += list(permutations(nums,i))
    new_lst = set([int("".join(p)) for p in pm])
    for i in new_lst:
        if is_prime(i):
            answer.append(i)
    return len(set(answer))