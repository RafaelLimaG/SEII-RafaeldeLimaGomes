import numpy as np

data = np.loadtxt('spambase.csv', delimiter=",", dtype=np.float32)
print(data)
print(data.shape)

data = np.genfromtxt('spambase.csv', delimiter=",", dtype=np.float32)
print(data)
print(data.shape)