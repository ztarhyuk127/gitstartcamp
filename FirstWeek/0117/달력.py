import calendar

week_list = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
year = int(input())
if calendar.isleap(year) == True :
    print("윤년입니다. 연도를 다시 입력해주세요.")
else :
    month = input()
    day = input()
    if month == '' and day == '':
        print(calendar.calendar(year))
    else :
        monthint = int(month)
        dayint = int(day)
        yoil = week_list[calendar.weekday(year,monthint,dayint)]
        if yoil == '월요일' :
            print("경고 월요일입니다.")
        datedict = {'년' : year,'월': monthint,'일':dayint, '요일': yoil}
        print(datedict)
