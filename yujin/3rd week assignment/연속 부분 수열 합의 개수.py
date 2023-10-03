def solution(elements):
    sum_n = set()
    for n in range(len(elements)):
        for i in range(len(elements)):
            if n + i > len(elements):
                e_sum = sum(elements[i:]) + sum(elements[:i + n - len(elements)])
            else:
                e_sum = sum(elements[i:i + n])
            sum_n.add(e_sum)
    return len(sum_n)