import numpy as np
import matplotlib.pyplot as plt

# interval 
a = 0
b = 5

# partition size 
n = 1000
delta = (b - a) / n

# axis
part = np.linspace(a, b, n+1)

# f(x) = sin(x^2)
func = part
func = func ** 2
func = np.sin(func)

# nice increments 
dfunc = np.zeros(n)
for i in range(n):
    dfunc[i] = func[i + 1] - func[i]

# plot
plt.plot(part[:n], dfunc)
plt.title('Increments, $df(x_i) = f(x_i) - f(x_{i-1})$, for $f(x) = \sin(x^2)$')
plt.show()
