def solution(n, left, right):
    result = []
    for index in range(left,right+1):
        row = index//n 
        column = index%n 
        if row<column: row,column =column,row
        result.append(row+1)
    
    return result