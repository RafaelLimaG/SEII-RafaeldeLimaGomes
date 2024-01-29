# Array x List

import numpy as np

l = [1,2,3]
a = np.array([1,2,3])

# No list:
l.append(4)
print(l)
l = l + [5]
print(l)

# No np.array (adiciona 4 a cada elemento)
a = a + np.array([4])
print(a)

# No list:
l = l * 2
print(l)


# No np.array:
a = a * 2
print(a)


a = np.sqrt(a)
print(a)
