def solution(a, b):
    answer = ''
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    days = b-1
    
    for month in range(1, a):
        days += month_day[month]
    answer = day[days%7]
    return answer
