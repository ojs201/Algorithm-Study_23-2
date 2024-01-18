import math

def solution(n, k):
    answer = []
    people = [i+1 for i in range(n)]
    answer = decideFirstPerson(people, k)
    return answer

def decideFirstPerson(people, k):
    if(len(people) == 1):
        return people
    idxOfFirstPerson = (k-1)//math.factorial(len(people)-1)
    k -= idxOfFirstPerson*math.factorial(len(people)-1)
    return [people.pop(idxOfFirstPerson)] + decideFirstPerson(people, k)
    
#1. 제일 앞자리 사람부터 결정한다. 
#2. 4명을 세운다고 할 때,  1 ~> (2,3,4 순열)
#                    2 ~> (1,3,4 순열)
#                    3 ~> (1,2,4 순열)
#                    4 ~> (1,2,3 순열)
#3. 과 같이 뒤에 사람를 배치하는 개수를 넘어가면 맨 앞자리가 다음 숫자로 넘어간다.
#4. 따라서 구해야 하는 순서인 k를 뒤에 사람를 배치하는 개수로 나누면 첫 번째 사람을 구할 수 있다.

#제일 앞자리 사람이 3이라고 할때, 이제 3을 제외한 (1,2,4 순열) 중에서 k-(제일 앞자리가 3미만인 경우의 개수)번째 를 찾으면 된다. -> 재귀사용(1,2,3,4 과정 진행)
import math

def solution(n, k):
    answer = []
    people = [i+1 for i in range(n)]
    answer = decideFirstPerson(people, k)
    return answer

def decideFirstPerson(people, k):
    if(len(people) == 1):
        return people
    idxOfFirstPerson = (k-1)//math.factorial(len(people)-1)
    k -= idxOfFirstPerson*math.factorial(len(people)-1)
    return [people.pop(idxOfFirstPerson)] + decideFirstPerson(people, k)
    
#1. 제일 앞자리 사람부터 결정한다. 
#2. 4명을 세운다고 할 때,  1 ~> (2,3,4 순열)
#                    2 ~> (1,3,4 순열)
#                    3 ~> (1,2,4 순열)
#                    4 ~> (1,2,3 순열)
#3. 과 같이 뒤에 사람를 배치하는 개수를 넘어가면 맨 앞자리가 다음 숫자로 넘어간다.
#4. 따라서 구해야 하는 순서인 k를 뒤에 사람를 배치하는 개수로 나누면 첫 번째 사람을 구할 수 있다.

#제일 앞자리 사람이 3이라고 할때, 이제 3을 제외한 (1,2,4 순열) 중에서 k-(제일 앞자리가 3미만인 경우의 개수)번째 를 찾으면 된다. -> 재귀사용(1,2,3,4 과정 진행)
