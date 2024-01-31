import numpy as np

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors)

b = eigenvectors[:,0] * eigenvalues[0]
print(b)

c = a @ eigenvectors[:,0]
print(c)

print(b==c)
print(np.allclose(b,c))

A = np.array([[1,1], [1.5 , 4.0]])
b = np.array([2200, 5050])

print(A ,'=', b)

x1 = np.linalg.inv(A).dot(b)
print(x1)

x2 = np.linalg.solve(A, b)
print(x2)