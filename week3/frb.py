import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fac

mu = np.arange(0,0.1,0.0001)
dmu = mu[1]-mu[0]
prior = np.ones(mu.shape)
likelihood = 100*mu*np.exp(-100*mu) #k=1
evidence = dmu*np.sum(likelihood*prior)
posterior = likelihood*prior/evidence


plt.plot(mu,posterior,linewidth=1.5)
plt.xlabel(r"$\mu\,\, [{\rm deg}^{-2}\,{\rm hr}^{-1}]$")
plt.ylabel(r"${\rm PDF}(\mu|E)$")
plt.tight_layout()
plt.savefig("frb.png")
plt.show()
plt.close()


k = np.arange(0,70,1.0)
yld = np.zeros(k.shape)
for i in range(len(k)):
   yld[i] = dmu * np.sum(posterior*np.exp(-1000*mu)*(1000*mu)**k[i]/fac(int(k[i])))

plt.stem(k,yld)
plt.xlabel("Expect FRB yield")
plt.ylabel("Probability")
plt.tight_layout()
plt.savefig("frb2.png")
plt.show()
plt.close()
