import numpy as np 

lst = [1, 2, 3]
arr = np.array([10, 20, 30, 40, 50])

print(lst)
print(arr)

print(arr.shape)
print(arr*2)
print(arr.mean())
print(arr[0])


print(arr[1:3])
print(arr[:3])
print(arr[::2])

mat =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat)

print(mat[0,0])
print(mat[2,1])

print(mat[1])
print(mat[:,2])

print(mat[0:2,1:3])

arr1 = np.array([5, 10, 15, 20, 25])

mask= arr1>15
print(mask)

print(arr1[mask])

print(arr1[arr1%10==0])

arr1[arr1>15]=90
print(arr1)

res = np.where(arr1>15,1,0)
print(res)

arr2 = np.arange(0,7)
print(arr2)

# reshape =  arr2.reshape(5,-1)
# reshapeauto =arr2.reshape(4,-1)

# print(reshape)
# print(reshapeauto)

flat =arr2.flatten()
flat[0]=999

print(flat)
print(arr2)

ravel= arr2.ravel()
ravel[0]=999

print(ravel)
print(arr2)

a = np.array([10, 20, 30, 40])
b=a[1:4]

print(a)
print(b)

c = a[1:4].copy()
c[0]=989

print(a)
print(c)

s =np.array([2,3,4,5,6])
print(s+5)

