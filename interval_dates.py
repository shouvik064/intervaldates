import datetime
import calendar

startdate = input("Enter start date? ")
startdate = datetime.datetime.strptime(startdate,"%Y%m%d").date()

enddate = input("Enter end date? ")
enddate = datetime.datetime.strptime(enddate,"%Y%m%d").date()

if (1900 <= startdate.year <= 2100) and (1900 <= enddate.year <= 2100):
  startyear = startdate.year
  startmonth = startdate.month
  endyear = enddate.year
  endmonth = enddate.month
  
  '''
  Calculation for 4th Saturday of the month
  '''
  for month in range(startmonth, endmonth+1):
    cal = calendar.monthcalendar(startyear, month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]
    fourth_week  = cal[3]
    fifth_week  = cal[4]
    if first_week[calendar.SATURDAY]:
      holi_day = fourth_week[calendar.SATURDAY]
      if holi_day % 5 != 0:
        print(str(startyear)+str(month)+str(holi_day))
    else:
      holi_day = fifth_week[calendar.SATURDAY]
      if holi_day % 5 != 0:
        print(str(startyear)+str(month)+str(holi_day))

  '''
  Calculation for Saturday and the date is multiple of 5
  '''
  while startdate <= enddate:
    if startdate.isoweekday() not in (1,2,3,4,5,7):
      if startdate.day % 5 == 0:
        weekOfMonth = startdate.isocalendar()[1] - startdate.replace(day=1).isocalendar()[1] + 1
        if weekOfMonth != 4:
          print(str(startdate.year)+str(startdate.month)+str(startdate.day))
    startdate += datetime.timedelta(days=1)
else:
  print("Please enter yaer within 1900 and 2100")