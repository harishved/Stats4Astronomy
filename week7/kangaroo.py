import numpy as np
import matplotlib.pyplot as plt
#
def l2(x):
   return np.log(x)/np.log(2)

x = np.arange(0,1./3,0.001)
H = -(x*l2(x) + 2*(1./3-x)*l2(1./3-x) + (1./3+x)*l2(1./3+x))

plt.plot(x,H,'k')
plt.xlabel(r"$p11$")
plt.ylabel(r"Shannon entropy [bits]")
plt.tight_layout()
plt.savefig("kangaroo.png")
plt.show()
plt.close()
