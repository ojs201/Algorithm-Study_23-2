# 할인 행사

from collections import defaultdict


def solution(want, number, discount):
    answer = 0

    db = defaultdict(int)
    for w, n in zip(want, number):
        db[w] = n

    db2 = defaultdict(int)
    for k in range(10):
        db2[discount[k]] += 1
        if db[discount[k]] == 0:
            db[discount[k]] = 0

    idx1 = 0
    idx2 = 10

    while 1:
        if db == db2:
            answer += 1
        if idx2 == len(discount):
            break

        db2[discount[idx1]] -= 1
        db2[discount[idx2]] += 1

        if db[discount[idx2]] == 0:
            db[discount[idx2]] = 0

        idx1 += 1
        idx2 += 1

    return answer