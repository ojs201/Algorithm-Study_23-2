def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        share, remainder = divmod(i, n)
        if(remainder <= share):
            answer.append(share+1)
        else:
            answer.append(remainder+1)
    return answer

#규칙 발견하는 과정
# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

# 1 => 0
# 2 => 1, 5, 5+1
# 3 => 2, 5+2, 10, 10+1, 10+2
# 4 => 3, 5+3, 10+3, 15, 15+1, 15+2, 15+3

# 5로 나눈 몫이 0일 때, 나머지+1 값 넣기
# 5로 나눈 몫이 1일 때, 나머지가 1보다 작거나 같으면 2 값 넣기,
#                             else      나머지값 +1 값 넣기
# 5로 나눈 몫이 2일 때, 나머지가 2보다 작거나 같으면 3 값 넣기
#                             else   나머지값 +1 값 넣기