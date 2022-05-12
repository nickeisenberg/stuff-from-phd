import matplotlib.pyplot as plt
import numpy as np

xaxisr = np.linspace(0, 5, 501)
xaxisl = -1 * np.flip(xaxisr)
xaxis = np.concatenate((xaxisl, xaxisr[1:]))


sigmar = xaxisr * np.log(xaxisr) 
sigmal = np.flip(sigmar)
sigma = np.concatenate((sigmal, sigmar[1:]))

xaxisrN = np.zeros((3, 501)) 

xaxisrN[0][:200] = xaxisr[:200]
for k in np.arange(201, 501, 1):
    xaxisrN[0][k] = 2
xaxis2 = np.concatenate((-1 * np.flip(xaxisrN[0]), xaxisrN[0][1:])) 
sigma2 = np.concatenate((np.flip(xaxisrN[0] * np.log(xaxisrN[0])), (xaxisrN[0] * np.log(xaxisrN[0]))[1:]))

xaxisrN[2][:300] = xaxisr[:300]
for k in np.arange(301, 501, 1):
    xaxisrN[2][k] = 3
xaxis3 = np.concatenate((-1 * np.flip(xaxisrN[2]), xaxisrN[2][1:])) 
sigma3 = np.concatenate((np.flip(xaxisrN[2] * np.log(xaxisrN[2])), (xaxisrN[2] * np.log(xaxisrN[2]))[1:]))

xaxisrN[1][:400] = xaxisr[:400]
for k in np.arange(401, 501, 1):
    xaxisrN[1][k] = 4
xaxis4 = np.concatenate((-1 * np.flip(xaxisrN[1]), xaxisrN[1][1:])) 
sigma4 = np.concatenate((np.flip(xaxisrN[1] * np.log(xaxisrN[1])), (xaxisrN[1] * np.log(xaxisrN[1]))[1:]))

fig = plt.figure()

ax1 = fig.add_subplot(222)
ax1.title.set_text('$\sigma_3(x)$')

ax2 = fig.add_subplot(221)
ax2.title.set_text('$\sigma_2(x)$')

ax3 = fig.add_subplot(223)
ax3.title.set_text('$\sigma_4(x)$')

ax4 = fig.add_subplot(224)
ax4.title.set_text('$\sigma(x) = |x| \log|x|$')

ax1.plot(xaxis, sigma3)
ax1.set_ylim(-1,9)

ax2.plot(xaxis, sigma2)
ax2.set_ylim(-1,9) 

ax3.plot(xaxis, sigma4)
ax3.set_ylim(-1,9) 

ax4.plot(xaxis, sigma)
ax4.set_ylim(-1,9) 

# fig.suptitle('Plots of $\sigma_N$ and $\sigma(x) = |x|\log|x|$')
plt.show()


