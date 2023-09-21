# <풀이 과정>

# brown과 yellow의 합은 총 넓이와 같다.
# 따라서, 두 넓이가 될 수 있는, 가로(i)와 세로(j)를 찾아야 함.
# 이때, 가로가 세로보다 크거나 같아야 하므로, 편의상 for문을 내림차순으로 해주었다.
# 조건식으로는, 1) 세로가 가로보다 클때 break; 2) (i-2)*(j-2)가 yellow와 같을때 return


def solution(brown, yellow):
    answer = []
    
    sum = brown+yellow
    
    for i in range(sum-1, 1, -1):
        if sum%i == 0:
            j = sum//i
            if j > i:
                break
            elif (i-2)*(j-2) == yellow:
                answer = [i,j]
                
    return answer