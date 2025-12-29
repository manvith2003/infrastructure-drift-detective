import numpy as np

a = np.array([1, 4, 9, 36])

print(np.sqrt(a))
print(np.log(a))
print(np.exp(a))


print(a.sum())
print(a.mean())
print(a.var())
print(a.std())

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.sum(mat,axis=0))
print(np.sum(mat,axis=1))

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])


print(A@B)
print(A*B)
print(A.T)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(np.dot(x,y))

print(np.linalg.det(A))
print(np.linalg.inv(A))

np.random.seed(42)
print(np.random.rand(5))