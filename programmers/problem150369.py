def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = n-1
    clean = n-1
    while delivery >= 0 or clean >= 0:
        distance = -1
        cur = cap
        while delivery >= 0:
            if deliveries[delivery] > 0:
                distance = max(distance, delivery)
                if cur - deliveries[delivery] > 0:
                    cur -= deliveries[delivery]
                    delivery -= 1
                else:
                    deliveries[delivery] -= cur
                    break
            else:
                delivery -= 1
        cur = cap
        while clean >= 0:
            if pickups[clean] > 0:
                distance = max(distance, clean)
                if cur - pickups[clean] > 0:
                    cur -= pickups[clean]
                    clean -= 1
                else:
                    pickups[clean] -= cur
                    break
            else:
                clean -= 1
        answer += (distance + 1)*2
    return answer
