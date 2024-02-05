"""
LV2. 광물 캐기
[https://school.programmers.co.kr/learn/courses/30/lessons/172927]


[풀이]
1. 광물을 5개 단위의 그룹으로 묶고 처리 가능한 범위로 제한한다.
2. 각 그룹을 (다이아-철-바위)의 개수를 기준으로 내림차순 정렬시킨다.

    - 위와 같이 정렬하면 높은 비용을 가진 광물들부터 처리할 수 있다.
    - e.g. before:
            [["stone", "iron", "diamond", "stone", "iron"], -> (다이아1, 철2, 돌1)
            ["diamond", "diamond", "stone", "stone", "stone"]] -> (다이아2, 돌3)
    - e.g. after:
            [['diamond', 'diamond', 'stone', 'stone', 'stone'],
            ['stone', 'iron', 'diamond', 'stone', 'iron']]

3. 정렬시킨 광물들을 (다이아-철-돌) 곡괭이 순으로 선택하여 비용을 계산한다.
"""
pick_mapper = [
    {"diamond": 1, "iron": 1, "stone": 1},
    {"diamond": 5, "iron": 1, "stone": 1},
    {"diamond": 25, "iron": 5, "stone": 1}
]


def pick_cost(pick_type, minerals):
    return sum([pick_mapper[pick_type][minaral] for minaral in minerals])


def solution(picks, minerals):
    minerals = [minerals[i:i + 5] for i in range(0, len(minerals), 5)][:sum(picks)]
    minerals = sorted(
        minerals,
        key=lambda subset: (
            subset.count('diamond'),
            subset.count('iron'),
            subset.count('stone')
        ),
        reverse=True
    )
    print(minerals)

    dia_picks, iron_picks, stone_picks = picks
    answer = 0

    for mineral_subset in minerals:
        if dia_picks > 0:
            answer += pick_cost(0, mineral_subset)
            dia_picks -= 1
        elif iron_picks > 0:
            answer += pick_cost(1, mineral_subset)
            iron_picks -= 1
        elif stone_picks > 0:
            answer += pick_cost(2, mineral_subset)
            stone_picks -= 1

    return answer
