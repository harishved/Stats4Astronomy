import numpy as np
import matplotlib.pyplot as plt

tp = np.load("rv.npz")
A = tp["A"]
sig = tp["err"]
t = tp["t"]
rv = tp["rv"]
per = tp["per"]


#xstart = np.random.rand(5)
xstart = np.arange(0.7,0.8,0.02)
for j in range(len(xstart)):
   x = xstart[j]
   p2 = 2*np.pi
   iiter = 0
   vals = []
   vals.append(x)
   for i in range(10):
      st = np.sin(p2*x*t)
      ct = np.cos(p2*x*t)
      dl = np.sum(p2*t*st*(rv-ct))
      dl2 = np.sum((p2*t*st)**2 + (p2*t)**2*ct*(rv-ct))
      x = x-dl/dl2
      vals.append(x) 
      iiter+=1

   plt.plot(vals,'kx-')
   chi2 = sig**-2*np.sum((rv-ct)**2)
   plt.text(s=r"$\chi^2=%.2f$"%chi2,x=iiter-2,y=vals[-1]*1.01)
plt.xlabel("Iteration number")
plt.ylabel("Frequency estimate [1/yr]")
plt.title("Gradient descent for different initial guesses",fontsize=12)
plt.tight_layout()
plt.savefig("rv_guesses.png")
plt.show()
plt.close()

