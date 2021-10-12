def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities_idx = 0
    if cacheSize == 0:
        answer = 5 * len(cities)
    else:
        while len(cache) < cacheSize and cities_idx < len(cities):
            if cities[cities_idx].upper() in cache:
                cache.remove(cities[cities_idx].upper())
                cache.append(cities[cities_idx].upper())
                answer = answer + 1
            else:
                cache.append(cities[cities_idx].upper())
                answer = answer + 5
            cities_idx = cities_idx + 1
        while cities_idx < len(cities):
            if cities[cities_idx].upper() in cache:
                cache.remove(cities[cities_idx].upper())
                cache.append(cities[cities_idx].upper())
                answer = answer + 1
            else:
                del cache[0]
                cache.append(cities[cities_idx].upper())
                answer = answer + 5
            cities_idx = cities_idx + 1
    return answer