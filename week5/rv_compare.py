import numpy as np
import matplotlib.pyplot as plt
#
Afit = 1.17
phifit = -0.24
Pfit = 0.77
#
tp = np.load("rv.npz")
Areal = tp["A"]
phireal = 0
Preal = tp["per"]
t = tp["t"]
rvreal = tp["rv"]
err = tp["err"]

tp = np.load("samples.npz")
samples = tp["x"]
x = samples[::10000,:]

tvec = np.linspace(np.amin(t),np.amax(t),500)
plt.figure(figsize=(4.5,4.5))
plt.subplot(211)
bestfit =  Afit*np.cos(2*np.pi*tvec*Preal+phireal)
for i in range(len(x[:,0])):
   plt.plot(tvec,x[i,0]*np.cos(2*np.pi*x[i,1]*tvec+x[i,2]),'0.5',linewidth=0.5,alpha=0.5)
plt.plot(tvec,bestfit, 'm', linewidth=1.5)
plt.errorbar(x = t, y = rvreal, yerr = err, fmt="ko")
plt.ylabel(r"rv [m/s]")
plt.subplot(212)
plt.errorbar(x = t,y = rvreal-Afit*np.cos(2*np.pi*t*Preal+phireal), yerr = err, fmt = "ko")
plt.axhline(y=0)
plt.xlabel(r"Orbital Frequency [yr$^{-1}$]")
plt.ylabel("rv residual [m/s]")
plt.tight_layout()
plt.savefig("rv_fits.png")
plt.show()
plt.close()
