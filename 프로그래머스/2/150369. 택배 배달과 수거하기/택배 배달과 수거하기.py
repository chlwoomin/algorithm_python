def solution(cap, n, deliveries, pickups):
    answer = 0
    # cap 값 저장
    cap_copy = cap
    # 한 번 배달
    while deliveries or pickups:
        distance1 = 0
        cap = cap_copy
        while deliveries and cap > 0:
            delivery = deliveries.pop()
            if delivery != 0 and distance1 == 0:
                distance1 = len(deliveries) + 1
            if cap >= delivery:
                cap -= delivery
            else:
                delivery -= cap
                cap = 0
                deliveries.append(delivery)
        
        cap = cap_copy
        distance2 = 0
        while pickups and cap > 0:
            pickup = pickups.pop()
            if pickup != 0 and distance2 == 0:
                distance2 = len(pickups) + 1
            if cap >= pickup:
                cap -= pickup
            else:
                pickup -= cap
                cap = 0
                pickups.append(pickup)
        answer+= distance1 + distance2 + (max(distance1, distance2) - min(distance1, distance2))
    return answer