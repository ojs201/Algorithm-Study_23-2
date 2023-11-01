def isPrimeNumber(w):
    for i in range(2,int(int(w)**0.5)+1):
        if int(w)%i==0:
            return False
    return True                    

def solution(n, k):
    answer = 0
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base = str(mod) + base

    for number in base.split("0"):
        if(len(number) != 0 and int(number) != 1):
            if(isPrimeNumber(int(number))):
                answer += 1
    return answer
