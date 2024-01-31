import numpy as np

a = np.array([1,2])
print(a.shape)

b = np.array([[1,2,3,4], [3,4,2,1]])
print(b.shape)

print(b[0][2])
print(b[0,2])
print(b[:,0])
print(b[0,:])
print(b.T)

c = np.array([[1,2],[4,5]])
print(np.linalg.inv(c))
print(np.linall.det(c))
print(np.diag(c))

d = np.diag(c)
print(np.diag(d))
