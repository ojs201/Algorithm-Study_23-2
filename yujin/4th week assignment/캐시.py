def solution(cacheSize, cities):
    e_time = 0
    cache = []
    if cacheSize == 0: 
       return len(cities) * 5
    for city in cities:
      if city.lower() in cache:
        cache.remove(city.lower())
        cache.append(city.lower())
        e_time += 1
      else:
        if len(cache) == cacheSize: cache.pop(0) 
        cache.append(city.lower())
        e_time += 5

    return e_time