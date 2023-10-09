# 나의 1차 풀이 80/100
# 모든 경우를 다 고려했지만, test_case 11 16 19 20 틀림.
from collections import deque

# LRU : 가장 오랫동안 참조되지 않은 페이지를 교체
def solution(cacheSize, cities):
    time = 0
    cache = deque()
    
    for city in cities: 
        
        # 대소문자 구분하지 않기 때문에 소문자로 애초에 변환해서 시작.
        city = city.lower()
        
        if cacheSize == 0:
            time = len(cities)*5
            break
        # cacheSize가 cities의 길이보다 큰 경우를 고려 -> 얘 때문에 test_case 11 16 19 20 에러 
        elif cacheSize > len(cities):
            if city in cache:
                time += 1
            else:
                cache.append(city)
                time += 5
        elif len(cache) == cacheSize and city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        elif len(cache) == cacheSize and city not in cache:
            cache.popleft()
            cache.append(city)
            time += 5        
        else: 
            cache.append(city)
            time += 5
        
    return time
        

# 나의 2차 풀이
def solution(cacheSize, cities):
    time = 0
    cache = []

    for city in cities:
        city_lower = city.lower()  # 대소문자 구분을 위해 소문자로 변환
        if cacheSize == 0:
            time += 5
        elif city_lower in cache:
            cache.remove(city_lower)
            cache.append(city_lower)
            time += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)  # 캐시가 꽉 찼을 때, 가장 오래된 항목을 삭제
            cache.append(city_lower)
            time += 5

    return time