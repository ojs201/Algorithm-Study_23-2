def solution(arr1, arr2):
    row = len(arr1)
    column = len(arr2[0])
    answer = [[] for _ in range(row)]
    for y in range(row):
        for x in range(column):
            temp = 0
            for i in range(len(arr2)):
                temp += arr1[y][i]*arr2[i][x]
            answer[y].append(temp)
    return answer

# 최종 행렬의 크기는 arr1의 행 개수*arr2의 열 개수
# [a][b]은 arr1의 a번째 행에 있는 수 * arr2의 각 행의 b번째의 총 합