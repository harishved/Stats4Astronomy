# Statistics for Astronomy: Chapter 3
# Author: Harish Vedantham
#
# Peculiar properties of the Cauchy distribution
#
import numpy as np
import matplotlib.pyplot as plt
#
N = 1000 # Number of samples to draw
#
g = np.random.randn(N)
c = np.random.standard_cauchy(N)
#
plt.figure(figsize=(6,4))
# Plot the two PDFs (Gaussian and Cauchy)
plt.subplot(121)
x = np.arange(-5,5,0.01)
plt.plot(x,(2*np.pi)**-0.5*np.exp(-x**2/2),'-',label="Gaussian")
plt.plot(x,np.pi**-1*(1+x**2)**-1,label="Cauchy")
plt.legend()
plt.xlabel(r"$X$")
plt.ylabel(r"${\rm PDF}(X)$")
#
# Compute the running mean and std for the two set of samples
plt.subplot(122)
g_mean = np.zeros(g.shape)
g_std = np.zeros(g.shape)
c_mean = np.zeros(c.shape)
c_std = np.zeros(c.shape)
#
for i in range(N):
   g_mean[i] = np.mean(g[:i])
   g_std[i] = np.std(g[:i])
   c_mean[i] = np.mean(c[:i])
   c_std[i] = np.std(c[:i])

x = np.arange(N)+1
plt.step(x,g_mean,label="Gaussian mean")
plt.step(x,g_std,label="Gaussian st. dev.")
plt.step(x,c_mean,label="Cauchy mean")
plt.step(x,c_std,label="Cauchy st. dev.")

plt.legend()
plt.xlabel("Number of samples")
plt.ylabel("Statistic")
plt.tight_layout()
plt.savefig("cauchy.png")
plt.show()
plt.close()
