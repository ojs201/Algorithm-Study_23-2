# 1차시도 -> 실패
# def solution(n ,a ,b):
#     cnt = 0
#     while True:
#         if (a+1) // 2 == 1 and (b+1) // 2 == 2:
#             cnt += 1
#             break
#         else:
#             cnt += 1
#             a = (a+1) // 2
#             b = (b+1) // 2
 
#     return cnt


# 2차 시도 -> 성공
def solution(n ,a ,b):
    cnt = 0
    while a != b:
            cnt += 1
            a = (a+1) // 2
            b = (b+1) // 2
 
    return cnt


