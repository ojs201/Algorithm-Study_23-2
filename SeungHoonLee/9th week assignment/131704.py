"""
LV2. 택배상자
[https://school.programmers.co.kr/learn/courses/30/lessons/131704]

풀이:
1. order를 역순으로 저장하는 스택(order_boxes)을 만든다.
2. 보조 컨테이너를 나타내는 스택(sub_boxes)을 만든다.
3. 1번째 상자부터 (order의 크기)번째의 상자까지 아래 연산을 적용한다.
    (이때, answer = 현재 트럭에 실린 상자의 개수)

    3.1 N번째 상자를 보조 컨테이너에 저장한다.
    3.2 보조 컨테이너 최상단에 저장된 상자와 order_boxes의 최상단에 저장된 상자를 비교한다.
        3.3.A
            - 두 상자가 다르다면 <3.1> 과정으로 돌아간다.
        3.3.B
            - 두 상자가 같다면 보조 컨테이너와 order_boxes의 상자를 지우고 answer를 +1한다.
            - <3.2> 과정으로 돌아간다.
"""


def solution(order):
    order_boxes = order[::-1]
    sub_boxes = []
    answer = 0

    for box in range(1, len(order) + 1):
        sub_boxes.append(box)

        while sub_boxes and sub_boxes[-1] == order_boxes[-1]:
            order_boxes.pop()
            sub_boxes.pop()
            answer += 1

    return answer
