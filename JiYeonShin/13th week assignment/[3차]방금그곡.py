code = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
codeDict = {}
for i in range(len(code)):
    codeDict[code[i]] = i

def solution(m, musicinfos):
    maxPlayTime = 0
    answer = '(None)'
    for musicinfo in musicinfos:
        startTime, endTime, title, music = musicinfo.split(",")
        music_intcode = changeToIntCode(music)
        playTime = calPlayTime(startTime, endTime)
        share, remain = divmod(playTime, len(music_intcode))
        melody = music_intcode*share + music_intcode[:remain]
        if(changeToIntCode(m) in melody): #노래 찾음
            if(playTime > maxPlayTime):
                maxPlayTime = playTime
                answer = title  
    return answer

def changeToIntCode(music):
    return music.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
        
def calPlayTime(startTime, endTime):
    start = startTime.split(':')
    end = endTime.split(':')
    return (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
    