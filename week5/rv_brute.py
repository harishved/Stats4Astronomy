import numpy as np
import matplotlib.pyplot as plt

tp = np.load("rv.npz")
A = tp["A"]
sig = tp["err"]
t = tp["t"]
rv = tp["rv"]
per = tp["per"]

pvec= np.arange(0.4,1.4,0.005)
ll = np.zeros(pvec.shape)
for i in range(len(pvec)):
   ll[i] = -sig**-2*np.sum((rv-np.cos(2*np.pi*pvec[i]*t))**2)

ll-=np.amax(ll)

plt.plot(pvec,ll,'k')
plt.xlabel("Trial frequency [1/year]")
plt.ylabel("Log-likelihood")
plt.tight_layout()
plt.savefig("rv_brute.png")
plt.show()
plt.close()
