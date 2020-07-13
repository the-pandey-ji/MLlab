import numpy as np

arr1=np.array([1,2,3,4,np.nan,5,np.nan])
print(arr1)
arr2=np.isnan(arr1)
print(arr2)
arr2=~arr2
print(arr2)
arr=arr1[arr2]
print(arr)
