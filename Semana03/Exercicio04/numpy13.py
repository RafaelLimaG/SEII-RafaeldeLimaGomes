import numpy as np

a = np.array([1,2,3])
print(a)

b = a
b[0] = 42
print(b)
print(a)

a = np.array([1,2,3])
print(a)

b = a.copy()
b[0] = 42

print(b)
print(a)