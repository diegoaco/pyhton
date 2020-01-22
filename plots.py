import numpy as np
import matplotlib.pyplot as plt

# Define a partition (values of x are put on an array)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

# Define the cosine and sine functions
C, S = np.cos(x), np.sin(x)

plt.plot(x, C)
plt.plot(x, S)

plt.show()
