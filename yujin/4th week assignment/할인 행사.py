def solution(want, number, discount):
    cnt = 0
    new_want = []
    for i in range(len(want)):
        for _ in range(number[i]):
            new_want.append(want[i])
        new_want.sort()
    for j in range(len(discount)):
        discount_10 = discount[j:j+10]
        discount_10.sort()
        if new_want == discount_10:
            cnt += 1
    return cnt