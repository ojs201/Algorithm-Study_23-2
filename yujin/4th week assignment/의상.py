def solution(clothes):
    clothes_cnt = {}
    for cloth in clothes:
        if cloth in clothes_cnt:
            clothes_cnt[cloth] += 1
        else:
            clothes_cnt[cloth] = 1
    total_cloth = 1
    for count in clothes_cnt.values():
        total_cloth *= (count + 1)
    total_cloth -= 1

    return total_cloth