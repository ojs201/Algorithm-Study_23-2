#문제에 쓰여있는 대로 1,2,3 과정 데이터 전처리 후 
#파이썬 bitwise XOR ^연산자 이용 

def solution(data, col, row_begin, row_end):
    answer = 0
    li = []
    data.sort(key = lambda x : (x[col-1], -x[0]))
    for i in range(row_begin-1, row_end):
        li.append(sum(map(lambda x : x%(i+1), data[i])))
    bit = li[0]
    for j in li[1:]:
        bit = bit ^ j
    return bit
