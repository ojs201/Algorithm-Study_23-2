def solution(n):
    answer = 0
    Ones = countOnesInBinary(n)
    for i in range(n+1, 1000001):
        if(countOnesInBinary(i) == Ones):
            answer = i
            break
    return answer

def countOnesInBinary(n):
    return bin(n)[2:].count("1")