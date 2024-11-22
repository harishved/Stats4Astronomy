import numpy as np
import matplotlib.pyplot as plt
#
N=20
A = 1.0
phi_0 = 0.0
per = 0.76
err= 0.5
#
t = np.sort(np.random.rand(N)*10) # time in years
rv = A*np.cos(2*np.pi*per*t)+np.random.randn(N)*err


np.savez("rv.npz",t=t,err=err,A=A,per=per,rv=rv)
plt.errorbar(x=t,y=rv,yerr=err,fmt="ko")
plt.xlabel("Time [years]")
plt.ylabel("Radial Velocity [m/s]")
plt.title("Mock RV data")
plt.tight_layout()
plt.savefig("rv.png")
plt.show()
plt.close()

