# 1차 풀이 -> 실패
# 로직 상 문제가 없어보이는데, 틀렸다고 한다...
# def solution(citations):
#     result = 0
    
#     li = [i for i in range(min(citations), max(citations)+1)] #인덱싱을 위한 리스트
    
#     for i in li:
#         over_num = 0
#         under_num = 0
#         for j in sorted(citations):
#             if i==j:
#                 over_num+=1
#                 under_num+=1
#             elif j>i:
#                 over_num += 1
#             elif j<i:
#                 under_num += 1
        
#         #print(i, over_num, under_num)
#         if i==over_num==under_num:
#             return i
        

# 2차 풀이
def solution(citations):
    citations.sort(reverse=True)  # citations 배열을 내림차순으로 정렬

    h_index = 0  # H-Index 초기값

    # 현재 논문의 인용 횟수가 현재 인덱스보다 크거나 같으면 H-Index를 업데이트하고, 
    # 그렇지 않으면 루프를 종료
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index
    
    
# 오름차순 정렬로 풀이한 풀이
def solution(citations):

    citations = sorted(citations)
    n = len(citations)

    for i in citations:
        if i >= n:
            break
        else:
            n -= 1
    answer = n        

    return answer
    