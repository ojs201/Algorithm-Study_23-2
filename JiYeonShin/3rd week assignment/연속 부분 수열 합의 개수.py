#시간초과
# def solution(elements):
#     answer = set()
#     n = len(elements)
#     for i in range(1, n):
#         for j in range(n):
#             #j부터 시작해서 i개를 더한 후 set에 추가
#             temp = 0
#             for k in range(i):
#                 temp += elements[(j+k)%n]
#             answer.add(temp)
#     return len(answer) + 1

def solution(elements):
    answer = set()
    n = len(elements)
    for i in range(n):
        temp = 0
        for j in range(n-1):
            temp += elements[(i+j)%n]
            answer.add(temp)
    return len(answer) + 1