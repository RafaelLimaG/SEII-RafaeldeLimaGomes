import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-1000,1000,1)
print(x1)

plt.plot(x1, -x1**3+4)
plt.show()