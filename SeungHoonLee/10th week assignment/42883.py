"""
LV2. 큰 수 만들기
[https://school.programmers.co.kr/learn/courses/30/lessons/42883]

풀이:
1. 현재 수 number[i]에 대해 아래 조건에 만족하는지 검사한다.
    <1> stack{[..., ~ ,number[i-1]]} < number[i]
    -> <1> 번의 조건에 만족하는 경우, number[0] ~ number[i] 기준 가장 큰 숫자이다.

2. <1> 번 조건에 만족하는 경우, number[i]를 stack에 삽입한다, 그리고 k를 -1한다.
3. 위 1 ~ 2과정을 k가 0이 될 때까지 반복한다.
3. stack에 남아있는 숫자들 조합하여 반환한다.

[예외]
- k가 0이 아닐 경우, 스택에 가장 큰 숫자만 남지 않을 수 있다.

e.g. number = "91", k = 1
-> stack = ['9', '1'], k = 1

- 따라서 stack에 남아있는 후보를 뒤에서부터 k개 만큼 자른다.
- 이때 단순히 k개만큼 자르면 k가 0인 경우 오답이 반환된다.
- 따라서 다음과 같이 자른다. -> stack[:len(stack)-k]
"""


def solution(number, k):
    answer = []
    n = len(number)

    for i in range(n):
        while answer and k > 0 and answer[-1] < number[i]:
            answer.pop()
            k -= 1
        answer.append(number[i])

    return ''.join(answer)[:n - k]
