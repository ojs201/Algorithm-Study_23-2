# 제출때 실패

# def solution(people, limit):
#     cnt = 0
#     tmp = []
    
#     for i in range(len(people)):
#         for j in range(i+1, len(people)):
#             if people[i] + people[j] <= limit:
#                 cnt += 1
#                 tmp.append(people[i])
#                 tmp.append(people[j])
                
#     return len(people) - len(tmp) + cnt


def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        print(a, b)
        if people[b] + people[a] <= limit :
            print(people[b],  people[a])
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


# 인덱스를 start, end 시점으로 투 포인터로 접근

# while문의 조건을 보면 인덱스 같아지는 시점(people의 모든 요소 다 조사됨)을 a<b로 표현한 것도 자주 보는데 난 잘 못 씀ㅠㅠ

# 또 return 값이 결국 len(people) - answer인 것은 전체 한 번은 옮겨야 하는데 가장 가벼운 것과 가장 무거운 것이 묶어서 되는 경우는 2명이 한 보트로 처리되기 때문에 전체에서 그 경우를 빼주려고 한 것 같다.