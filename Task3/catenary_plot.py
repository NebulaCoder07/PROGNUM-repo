import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5,6,1)
y = [np.cosh(i) for i in x]
plt.title("Chain model made with NumPy")
plt.ylabel("y = Altitude [m]", fontsize = 12)
plt.xlabel("x = Position [m]", fontsize = 12)
plt.grid()
plt.plot(x, y, label="y = cosh(x)", color='green', marker = 'o')
plt.legend()
plt.show()
