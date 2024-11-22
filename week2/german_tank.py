# Statistics for Astronomy: Chapter -2
# German tank problem
#
import numpy as np
import matplotlib.pyplot as plt
#
k = 20 # Number of captured tanks
n = 112 # Peak serial number among captured tanks
#
Nmax = 40*n 	#Upper bound for the prior on sample size 
		# Try different values 
#
N = np.arange(n,Nmax,1.0)
#
prior = np.ones(N.shape) # Uniform prior
likelihood = np.zeros(N.shape)
for i in range(len(N)):
   likelihood[i] = k * np.prod(np.arange(n,n-k,-1.0))\
                   /np.prod(np.arange(N[i],N[i]-k,-1.0))

evidence = np.sum(prior*likelihood)
posterior = likelihood*prior/evidence
#
perlist = [50,90] # Perecentiles at which to draw lines in posterior plot
Nper = []
for per in perlist:
   integ = 1.0; i=0; # Area under the posterior
   while(integ>(100-per)/100):
      integ = np.sum(posterior[i:]);
      i+=1
   Nper.append(N[i])
   print ("%d percentile value = %f"%(per,Nper[-1]))
#
# Plot everything
plt.step(N,posterior,'k',linewidth=1.5)
plt.xlabel(r"$N$")
plt.ylabel(r"PDF$(N|E)$")
plt.title(r"$E:\, k=%d,\, n=%d$"%(k,n),fontsize=12)
for i in range(len(perlist)):
   plt.axvline(Nper[i])
   plt.text(x=1.01*Nper[i],y=posterior[0]/2,s=r"$%d^{\rm th}$ percentile"%perlist[i],rotation=90)
plt.xlim([n,Nper[-1]*1.1])
plt.tight_layout()
plt.savefig("german_tank.png")
plt.show()
plt.close()
