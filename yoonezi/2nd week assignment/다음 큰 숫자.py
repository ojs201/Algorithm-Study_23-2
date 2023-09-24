# n을 이진수로 변환 bin(n)[2:]
# 1의개수(O), 자릿수를 세기(X)
# 만약 101 이라면 세자리인거고, 세자리에서 1을 두개씩 사용해서 수를 계산하고 (X)
# n보다 더 큰 수가 없다면 자릿수 +1 , 반복? (X)

# n보다 큰 수 answer에 +1을 반복해가며 n의 이진법 변환 1의 개수와 같으면 break (O)

def solution(n):
    nBin = bin(n)[2:]
    oneCnt = nBin.count('1')
    answer = 0
    
    while True:
        n += 1
        nBin = bin(n)[2:]
        if oneCnt == nBin.count('1'):
            answer = n
            break

    return answer
