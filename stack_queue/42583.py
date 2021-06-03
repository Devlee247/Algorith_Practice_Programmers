def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    while True:
        sum_weight = 0
        for i in bridge:
            i[1] -= 1
            if i[1] != 0:
                sum_weight += i[0]
        for i in bridge:
            if i[1] == 0:
                bridge.pop(0)
        
        if len(bridge) < bridge_length and len(truck_weights) != 0 and sum_weight + truck_weights[0] <= weight:
            temp = [truck_weights.pop(0), bridge_length]
            bridge.append(temp)
        answer += 1
        if len(bridge) == 0:
            break
    
    return answer
