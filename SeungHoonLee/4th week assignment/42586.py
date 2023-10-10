"""
LV2. 기능개발
[https://school.programmers.co.kr/learn/courses/30/lessons/17680]

풀이:
1. 각 기능별 완료 되는 날짜를 계산한다.
2. 각 계산한 완료 날짜에 따라 아래를 진행한다.

  A. 이전 기능의 완료 날짜 >= 현재 기능의 완료 날짜:
    - 이전 완료 날짜 보다 빠르게 끝나므로 이전 기능이 끝나는 시기에 같이 배포됨
    - 큐에 완료 날짜 삽입

  B. 이전 기능의 완료 날짜 < 현재 기능의 완료 날짜:
    - 현재 기능은 이전 기능이 배포된 후에 배포됨.
      - 즉 큐에 저장된 이전 기능들은 모두 현재 배포에 포함되는 기능의 수가 된다.
    - 따라서 현재 기능부터 다시 다음 배포일짜에 포함되므로 큐를 초기화
    - 큐에 완료 날짜 삽입
"""

from math import ceil


def solution(progresses, speeds):
    answer = []
    que = []

    for progress, speed in zip(progresses, speeds):
        remains_day = ceil((100 - progress) / speed)

        if que and que[0] < remains_day:
            answer.append(len(que))
            que.clear()

        que.append(remains_day)

    answer.append(len(que))
    return answer
