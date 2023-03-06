hour, min = map(int, input().split())
need_time = int(input())

answer = min + need_time

if (answer >= 60):
    if (hour+answer//60 >= 24):
        hour -= 24
    hour += answer//60
    print(hour, answer%60)
else: 
    if (hour >= 24):
        hour -= 24
    print(hour, answer)
