"""
LV2. 괄호 회전하기
[https://school.programmers.co.kr/learn/courses/30/lessons/76502]

풀이:
1. 문자열의 길이만큼 아래 과정을 반복한다.
  1.1. 문자열을 왼쪽으로 회전시킨다.
  1.2. 회전시킨 문자열이 올바른 괄호 문자열인지 검증한다.
    1.2.1 문자열에서 짝이 맞는 괄호('()', '{}', '[]')가 없을 때까지 제거한다.
    1.2.2.A 문자열이 공백이라면 올바른 괄호 문자열이므로 True를 반환한다.
    1.2.2.B 문지열이 공백이 아닐 경우 False를 반환한다.
  1.3. 올바른 괄호 문자열일 경우 +1씩 더한다.
2. 올바른 괄호 문자열의 갯수를 반환한다.
"""
def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += 1 if is_valid_parens(rotate_left(s, i)) else 0
    return answer

        
def rotate_left(s, step):        
    return s[step:] + s[:step]


def is_valid_parens(s):
    while True:
        if "()" in s:
            s = s.replace("()","")
        elif "{}" in s:
            s = s.replace("{}","")
        elif "[]" in s:
            s = s.replace("[]","")
        else:
            return False if s else True
