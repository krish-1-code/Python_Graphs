import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])

figure, axes = plt.subplots(2,2)

axes[0,0].plot(x,x**2)
axes[0,0].set_title("x**2")

axes[0,1].plot(x,x**3)
axes[0,1].set_title("x**3")

axes[1,0].plot(x,x**4)
axes[0,1].set_title("x**4")

axes[1,1].plot(x,x**5)
axes[0,1].set_title("x**5")
plt.show()