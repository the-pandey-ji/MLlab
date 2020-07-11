# import calendar
# yy= int(input("Enter year: "))
# mm = int(input("Enter month: "))
# print(calendar.month(yy, mm))

import calendar
yy= int(input("Enter year: "))
mm = int(input("Enter starting month: "))
mm1 = int(input("Enter ending month: "))
for i in range(mm,mm1+1):
    print(calendar.month(yy,i))