import numpy as np
import matplotlib.pyplot as plt

nu = np.arange(1.0,2.0,0.1)
atrue = -0.7
Strue = 1
err = 0.07
noise = np.random.randn(len(nu))*err
S = Strue*nu**atrue + noise

plt.errorbar(x=nu,y=S,yerr=err,fmt="ko")
plt.xlabel("Frequency [GHz]")
plt.ylabel("Flux density [Jy]")
plt.tight_layout()
plt.savefig("spind_data.png")
np.savez("spind.npz",S=S,nu=nu,err=err)
plt.show()
plt.close()
