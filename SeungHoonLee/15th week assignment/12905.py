"""
LV2. 가장 큰 정사각형 찾기
[https://school.programmers.co.kr/learn/courses/30/lessons/12905]

풀이:
다음 점화식을 활용한다.

: DP[i][j]
    = (i, j) 지점을 기준으로 최대 정사각형의 한 변의 길이
    = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1

예외:
- 문제에서 표가 모두 0 일 경우 만들 수 없는 정사각형이 없기 때문에 답은 0이 된다.
"""


def solution(board):
    if all(el == 0 for col in board for el in col):
        return 0

    answer = 1
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                answer = max(answer, board[i][j])

    return answer ** 2
