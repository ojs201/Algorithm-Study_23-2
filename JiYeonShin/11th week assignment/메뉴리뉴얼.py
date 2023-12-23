#====풀이 방법====
#우선 2명이상이 시킨 메뉴여야하므로 2중 for문 돌면서 교집합 찾기
#교집합 찾으면, 그 안에서 또 course에 맞는 조합들을 찾기
#해당 조합으로 시킨 손님의 수 계산하기
#현재 최대 주문한 코스에 대한 정보를 담고있는 coursesInfo와 비교하여 갱신해주기

#====coursesInfo 설명====
# 각 코스 종류 중에서 손님이 가장 많이 시킨 메뉴 구성을 구해야 한다. 
# 따라서 현재의 최대값들을 항상 유지하고 있어야 하기 때문에 
# 코스 종류를 key로 [현재 최대 주문 수, 메뉴구성 리스트]를 value로 하는 coursesInfo를 만들고 활용한다.
#메뉴구성을 리스트로 둔 이유는? 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아야 하기 때문입니다.


import itertools

def solution(orders, course):
    answer = []
    orderset = [set(order) for order in orders]
    coursesInfo = {} 
    for i in course:
        coursesInfo[i] = [0, []] #course개수, 현재 최대 주문 수, 코스메뉴구성리스트
    courseset = getCourseset(orderset, course)
    for c in courseset:
        cnt = getNumberOfOrdersForMenu(c, orderset)
        courseInfo = coursesInfo[len(c)]
        if(courseInfo[0] < cnt):
            courseInfo[0] = cnt
            courseInfo[1] = [c]
        elif(courseInfo[0] == cnt): 
            courseInfo[1].append(c)
    for courseInfo in coursesInfo.values():
        answer.extend(courseInfo[1])
    answer.sort()
    return answer

#코스요리 후보 모두 구하기
def getCourseset(orderset, course):
    courseset = set()
    for i in range(len(orderset)):
        for j in range(i+1, len(orderset)):
            courseMenuSet = orderset[i]&orderset[j]
            if(len(courseMenuSet) > 1):
                courseCombi = getCourseCombi(courseMenuSet, course)
                for c in courseCombi:
                    if(c in courseset):
                        continue
                    courseset.add(c)
    return courseset

def getCourseName(courseMenu):
    return "".join(sorted(list(courseMenu)))

#courseMenu에서 num개 뽑아서 courseCombi에 추가
def getCourseCombi(courseMenuSet, course):
    courseCombi = []
    courseMenuList = list(courseMenuSet)
    for num in course:
        comb = itertools.combinations(courseMenuList, num)
        courseCombi.extend(list(comb))
    return map(getCourseName, courseCombi)

#몇명의 손님이 해당 코스메뉴를 주문했는지 세기
def getNumberOfOrdersForMenu(c, orderset):
    cnt = 0
    courseMenu = set(c)
    for k in orderset:
        if(len(courseMenu - k) == 0):
            cnt += 1
    return cnt

