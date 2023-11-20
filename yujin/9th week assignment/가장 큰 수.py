# 실패한 코드
def solution(numbers):
    sorted_num = sorted(numbers, key=lambda x: str(x)[0])
    sorted_num.reverse()
    return str(int("".join(sorted_num)))
# ========================================================================================
def solution(numbers):
    num_lst = list(map(str,numbers))
    num_lst.sort(key=lambda x: x*3, reverse = True)
    return str(int("".join(num_lst)))