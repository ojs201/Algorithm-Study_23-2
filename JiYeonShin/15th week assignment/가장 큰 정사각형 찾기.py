#board를 돌면서 해당 자리를 끝 모서리로 가지는 가장 큰 정사각형의 넓이를 갱신해나간다. 

def solution(board):
    answer = 0
    row = len(board)
    column = len(board[0])
    dp = [[0 for _ in range(column)] for _ in range(row)]
    for y in range(row):
        for x in range(column):
            if(y == 0 or x == 0):
                dp[y][x] = board[y][x]
                continue
            if(board[y][x] == 1):
                dp[y][x] = min(dp[y-1][x-1], min(dp[y][x-1], dp[y-1][x]))+1
    length = max(map(lambda x : max(x), dp))
    answer = length**2
    return answer