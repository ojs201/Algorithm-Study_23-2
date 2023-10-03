# 나의 풀이
def solution(n,a,b):
    cnt = 1
    while True:
        a = (a//2) + (a%2)
        b = (b//2) + (b%2)
        if a == b:
            break
        cnt += 1
        
    return cnt

# 다른 사람의 풀이
def solution(n,a,b): 
	cnt = 0
	while a != b: 
		cnt += 1
        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 해서 나눴을때 몫이 1이 되도록
		a, b = (a+1)//2, (b+1)//2
	return cnt