# import calendar
# yy= int(input("Enter year: "))
# mm = int(input("Enter month: "))
# print(calendar.month(yy, mm))

# import calendar
# yy= int(input("Enter year: "))
# mm = int(input("Enter starting month: "))
# mm1 = int(input("Enter ending month: "))
# for i in range(mm,mm1+1):
#     print(calendar.month(yy,i))

# Multi-dimensional Array
import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
import sys

# memory occupied by list
s = range(1000)
print('memory occupied by List', sys.getsizeof(10) * len(s))
# memory occupied by numpy
d = np.arange(1000)
print('memory occupied by Numpy Array', d.size * d.itemsize)
print()