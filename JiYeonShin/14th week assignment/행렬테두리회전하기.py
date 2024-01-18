def solution(rows, columns, queries):
    answer = []
    arr = [[columns*j+i+1 for i in range(columns)] for j in range(rows)]
    for query in queries:
        start_y, start_x, end_y, end_x = map(lambda x : x-1, query)
        minNum = rows*columns
        number = rows*columns #다음에 저장해야 할 값
        temp = 0 #임시 저장
        for x in range(start_x, end_x+1):
            temp = arr[start_y][x]
            arr[start_y][x] = number
            number = temp
            minNum = min(minNum, number)
        for y in range(start_y+1, end_y+1):
            temp = arr[y][end_x]
            arr[y][end_x] = number
            number = temp
            minNum = min(minNum, number)
        for x in range(end_x-1, start_x-1, -1):
            temp = arr[end_y][x]
            arr[end_y][x] = number
            number = temp
            minNum = min(minNum, number)
        for y in range(end_y-1, start_y-1, -1):
            temp = arr[y][start_x]
            arr[y][start_x] = number
            number = temp
            minNum = min(minNum, number)
        answer.append(minNum)  
    return answer

#테두리 숫자들을 차례로 옮겨주면 되는 문제이다. 테두리 숫자들을 옮기며 가장 작은 수를 체크해준다.

# 2,2,5,4면
# 1,1,4,3 라고 생각하기
# minNum = rows*columns
# number = rows*columns #다음에 저장해야 할 값
# temp = 0 #임시 저장
# 1,1에서 1,3까지  => start_y, start_x  start_y, end_x
# 1+1,3에서 4,3까지 => start_y+1, end_x   end_y, end_x
# 4,3-1에서 4,1까지 => end_y, end_x-1    end_y, start_x
# 4-1,1에서 1,1까지 => end_y-1, start_x   start_y, start_x

# 자리의 값을 temp(14)에 저장 후, number(20)값 넣기, 그 후 number = temp2

# number값 갱신할 떄마다 minNum도 갱신

