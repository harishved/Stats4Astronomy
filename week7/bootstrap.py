import numpy as np
import matplotlib.pyplot as plt

Nb = 10000
x = np.array([1.209, 0.645, 0.788, 0.840, 0.930, 1.195, 0.597, 0.851, 1.107, 0.814, 0.695, 0.592, 0.752, 1.204, 1.205, 1.175, 0.920, 0.656, 1.240, 1.168])

print ("Sample mean = ", end = "")


print ("%.2f"%np.mean(x))

means = np.zeros(Nb)
for i in range(Nb):
   I = np.floor(np.random.rand(len(x))*19).astype(int)
   xb = np.array([x[j] for j in I])
   means[i] = np.mean(xb)

y1,x1 = np.histogram(means,bins=100)
y = y1.astype("float")
x = 0.5*(x1[1:]+x1[:-1])

bstd = np.std(means)
print ("Bootstrap std = %.2f"%bstd, end = "")
plt.step(x,y)
plt.xlabel("Bootstrap Means [Gyr]")
plt.ylabel(r"Estimated PDF [Gyr$^{-1}$]")
plt.tight_layout()
plt.savefig("bootstrap.png")
plt.close()
