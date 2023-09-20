# 첫번째 풀이
# 간단한 fibonacci 재귀함수로 구현 -> 시간초과 + 런타임에러
def solution(n):

    if n<2:
        return n
    else:
        return (solution(n-1) + solution(n-2))%1234567
    
# 두번째 풀이
# list 이용하여 풀기 -> O(n) 걸림
def solution(n):
    li = [0,1]
    
    for _ in range(n):
        li.append(li[-2]+li[-1])
    
    return li[n]%1234567


###########################################################################################################################


# 다른 사람의 풀이 -> 생각해보지 못한 Swapping...
def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(solution(100))
    
    
    
    
    
    
    