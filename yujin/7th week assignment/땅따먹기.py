def solution(land):
    l = len(land)
    for row in range(1,len(land)):
        for column in range(4):
            land[row][column] += max(land[row-1][column+1:]+land[row-1][:column])
    return max(land[l-1])