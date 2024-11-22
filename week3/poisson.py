import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fac
#
def poisson(l,klist):
   op = []
   for k in klist:
      op.append( np.exp(-l)*l**k/fac(k) )
   return np.array(op)
      

l_list = [1,3,5,10]
klist = np.arange(0,20,1).astype(int)
for l in l_list:
   plt.plot(klist,poisson(l,klist),'.-',label=r"$\lambda=%d$"%l)

plt.legend()
plt.xlabel(r"$k$")
plt.ylabel(r"${\rm Prob}(X=k)$")
plt.tight_layout()
plt.savefig("poisson.png")
plt.show()
plt.close()
