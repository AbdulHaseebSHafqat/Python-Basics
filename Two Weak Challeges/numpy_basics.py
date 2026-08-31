import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

print(type(arr1))
arr2 = np.array([[1,3,4],[5,7,8]])
print(arr2)
arr3 = np.zeros((2,3))
print(arr3)
arr4 = np.ones((3,3))
print(arr4)

arr5 = np.identity(5)
print(arr5)

arr6 = np.arange(10)
print(arr6)

arr7 = np.arange(5, 15)
print(arr7)


arr8 = np.arange(5, 16, 2)
print(arr8)

arr9 = np.linspace(10,20,10)
print(arr9)

arr10 = arr7.copy()
print(arr10)

print(arr1.shape)

print(arr3.shape)

print(arr5.shape)
print(arr2.shape)
print(arr2.shape)
print(arr6.shape)

arr11 = np.array([[[1,2] , [3,4] ], [[5,6] , [7,8]]])
print(arr11)
print(arr11.shape)

print(arr11.ndim)

print(arr1.ndim)
print(arr3.ndim)

print(arr9.size)
print(arr9.itemsize)
print(arr9.dtype)

lista = range(100)
arr20 = np.arange(100)
import sys

print(sys.getsizeof(87)*len(lista))
print(arr11.itemsize*arr20.size)

import time
x = range(10000000)
y = range(10000000 , 20000000)
start_time = time.time()
c = [(x,y) for x,y in zip(x,y)]
print(time.time() - start_time)

a = np.arange(10000000)
b = np.arange(10000000 , 20000000)
start_time = time.time()
c= a+b
print(time.time() - start_time)


arr21 = np.arange(24).reshape(6,4)
print(arr21)
print(arr21[2:3,1:3])
print("-----")

print(arr21[:,1:3])
print(arr21[2:3,1:3])
print(arr1[2:4])

for i in arr21:
    print(i)

for i in np.nditer(arr21):
    print(i)


arr22 = np.array([1,2,3,4,5,6])
arr23 = np.array([4,5,6,7,8,9])

print(arr22 -arr23)

print(arr22 * arr23)
print(arr22 * 2)
# print(arr22 = np.arange(6).reshape(2,3)
# print(arr23 = np.arange(6,12).reshape(3,2))
arr22.dot(arr23)

print(arr11)

print(arr11.ravel())

print(arr11.transpose())




