"""
LV2. [3차] 방금그곡
[https://school.programmers.co.kr/learn/courses/30/lessons/17683]

[풀이]
전체 [musicinfo]에 대해 아래 과정을 반복하여 수행하면서 <정답>을 찾는다.

    0. <정답>은 [제목]과 [총 재생 시간(최대)]를 갖는다.
        1. [제목]은 조건에 만족하는 음악 제목이다.
        2. [총 재생 시간(최대)]는 조건에 만족하는 음악 중 제일 긴 재생 시간의 값이다.

    1. 방송된 곡 정보에 대해 전처리를 수행한다.
        1. 총 재생 시간 (= 음악 끝난 시간 - 음악 시작 시간)을 구한다.
        2. 총 재생 시간에 따라 [악보 정보]를 반복한다.

    2. [악보 정보]에서 [m]이 존재하는지 판별한다.

    3. <2> 조건에 만족하는 경우 다음을 수행한다.

        3.A 조건에 일치하는 [악보 정보]가 없다면: 다음 비교로 넘어감
        3.B 곡의 [총 재생 시간]이 현재의 [가장 긴 재생 시간]보다 더 길때:
            - 현재 곡에 대한 [가장 긴 재생 시간]과 [제목]을 <정답>으로 설정한다.
"""


def solution(m, musicinfos):
    m = encode_melody(m)
    answer = {'title': '(None)', 'times': 0}

    for info in musicinfos:
        start, end, title, melody = info.split(',')
        playing_time = total_playing_time(start, end)
        melody = repeat_melody(encode_melody(melody), playing_time)

        if m in melody and answer['times'] < playing_time:
            answer = {'title': title, 'times': playing_time}

    return answer['title']


def encode_melody(melody):
    """
    멜로디에 대한 구분 및 비교를 위해 #코드를 별도로 인코딩
    """
    return melody \
        .replace('A#', 'a') \
        .replace('C#', 'c') \
        .replace('D#', 'd') \
        .replace('F#', 'f') \
        .replace('G#', 'g')


def total_playing_time(start, end):
    """
    총 재생 시간을 구한다.
    """
    s_hours, s_minutes = map(int, start.split(':'))
    e_hours, e_minutes = map(int, end.split(':'))
    return (e_hours - s_hours) * 60 + (e_minutes - s_minutes)


def repeat_melody(melody, playing_time):
    """
    주어진 반복 횟수에 따른 반복 재생된 멜로디를 구한다.

    - 음악 길이 > 재생 시간 -> 반복 재생된 멜로디
    - 음악 길이 < 재생 시간 -> 처음 ~ 재생 시간만큼의 멜로디
    """
    a, b = divmod(playing_time, len(melody))
    return encode_melody(melody * a + melody[:b])
