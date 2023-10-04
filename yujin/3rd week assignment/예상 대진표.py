# # 정확도 낮은 코드
# def solution(n,a,b):
#     arr = [0 for _ in range(n)]
#     arr[a-1] = 1
#     arr[b-1] = 1
#     cnt = 0
    
#     while n>1: # 변경하기
#         for i in range(n)[::2]:
#             a_sum = arr[i]+arr[i+1]
#             if a_sum == 2:
#                 break
#         cnt+=1
#         n=int(n/2)
#     return cnt

# ===============================================================================
# # a와 b가 다른 그룹에 속할 때마다 +1씩 하는 방법
def solution(n,a,b):
    round = 0
    
    while a != b:
        a=(a+1)//2
        b=(b+1)//2
        round += 1
    return round