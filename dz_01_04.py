import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 121)
plt.plot(x, np.cos(x))
z = x * 0.95
plt.plot(x, np.cos(z))
print(x, z)

