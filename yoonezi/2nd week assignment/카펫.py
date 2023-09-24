# 완전탐색

# 1차 시도 실패
# sum = y + b 
# for sum % if == 0 
# answer = [a > b]

# def solution(brown, yellow):
#     sum = brown + yellow
#     for i in range(1, sum+1):
#         if sum % i == 0:
#             tmp1 = i
#             tmp2 = sum / i
#             break
#     if tmp1 > tmp2:
#         a = tmp1
#         b = tmp2
#     else:
#         a = tmp2
#         b = tmp1
        
#     answer = [a, b]
#     return answer

# > yellow가 중앙에 있다는 것을 고려하지 않았음
# 나눌 수 있는 가장 

# 2차 실패..
# def solution(brown, yellow):
#     sum = brown + yellow
#     tmp = []
    
#     for i in range(1, sum+1):
#         if sum % i == 0:
#             tmp.append(i)
#     middle = (len(tmp) // 2)
#     answer = [tmp[middle], sum // tmp[middle]]
#     return answer


# 조건 :
# 1. a >= b
# 2. 2a + 2b - 4 = brown
# 3. (a-2) * (b-2) = yellow

# > 2a + 2b = brown + 4
# > ab - 2a - 2b + 4 = yellow
# => ab = yellow + brown



def solution(brown, yellow):
    answer = []
    
    sum = brown + yellow
    for b in range(1, sum+1):
        if (sum % b) == 0:
            a = sum // b
            if a >= b:
                if 2*a + 2*b == brown + 4:
                    return [a, b]
        
    return answer