thirties = [5, 7, 10, 11]
ans = 1-1
start_day = 1

for year in range(1901, 2001):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: isLeap = True
            else: isLeap = False
        else: isLeap == True
    else: isLeap = False
    
    for month in range(1, 13):
        if month == 2 and isLeap:
            start_day = (28 + start_day) % 7
        elif month == 2:
            start_day = (27 + start_day) % 7
        elif month in thirties:
            start_day = (29 + start_day) % 7
        else:
            start_day = (30 + start_day) % 7
        if start_day == 0: ans+=1
            
print(ans)
