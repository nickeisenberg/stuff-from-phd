import numpy as np
import matplotlib.pyplot as plt

# interval 
a = 0
b = 5

# partition 
n = 500 
delta = (b - a) / n

# time axis 
part = np.linspace(a, b, n+1)

# Brownian increments 
dB = np.sqrt(delta) * np.random.normal(0, 1, n)

# White noise 
dotW = np.zeros(n + 1)
dotW[1:] = dB

# plot 
plt.plot(part, dotW, linewidth=.5)
plt.title('White Noise: $dB_t$') 
plt.show()
