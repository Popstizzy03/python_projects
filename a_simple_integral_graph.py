import numpy as np
import matplotlib.pyplot as plt

# Example for part (a)
x = np.linspace(0, 1, 400)
y1 = 2 * np.ones_like(x)
y2 = 4 - 2 * x

plt.fill_between(x, y1, y2, color='lightblue')
plt.plot(x, y1, color='blue', label='y = 2')
plt.plot(x, y2, color='green', label='y = 4 - 2x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Region for part (a)')
plt.legend()
plt.grid(True)
plt.show()
