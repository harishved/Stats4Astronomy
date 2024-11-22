import numpy as np
import matplotlib.pyplot as plt
#
# Generate mock data
utrue = 25 # True initial velocity
atrue = 3.0 # True acceleration
#
t = np.arange(0.2,3.2,0.1) # Time
s = np.zeros(len(t)) # Distance vector
sig = np.zeros(len(t)) # Uncertainty sigma
#
for i in range(len(s)): # For each data point
   s[i] = utrue*t[i] - atrue*0.5*t[i]**2 # True distance
   sig[i] = (2+(0.05*s[i])**2)**0.5 # Uncertainty sigma
   s[i]+=np.random.randn()*sig[i] # True distance + noise
#
# Plot mock data
plt.errorbar(x=t,y=s,yerr=sig,fmt="ko")
plt.xlabel("Time [s]")
plt.ylabel("Distance travelled [m]")
plt.tight_layout()
plt.savefig("crash_data.png")
#plt.show()
plt.close()
#
#Max likelihood estimation
# model 1
u1_vec = np.arange(15,33,0.01)
ll1 = np.zeros(len(u1_vec))
for i in range(len(u1_vec)):
   ll1[i] = np.sum( (s-u1_vec[i]*t)**2/sig**2)
#
plt.plot(u1_vec,ll1/len(t),'k')
plt.xlabel(r"$u_1$ [m/s]")
plt.ylabel(r"$\chi^2(u_1)/N$")
plt.title("Model 1",fontsize=12)
plt.ylim([0,10])
e1 = 1.0/(33-15)*(u1_vec[1]-u1_vec[0])*np.sum(np.exp(-ll1/2))
plt.tight_layout()
plt.savefig("crash_ll1.png")
#plt.show()
plt.close()
#
#
u2_vec = np.arange(15,33,0.01)
a2_vec = np.arange(0,5.0,0.01)
ll2 = np.zeros((len(u2_vec),len(a2_vec)))
for i in range(len(u2_vec)):
   for j in range(len(a2_vec)):
      ll2[i,j] = np.sum( (s-u2_vec[i]*t+0.5*a2_vec[j]*t**2 )**2/sig**2  )

ext = [np.amin(a2_vec),np.amax(a2_vec),np.amin(u2_vec),np.amax(u2_vec)]
plt.imshow(ll2/len(t),aspect="auto",origin="lower",extent=ext,cmap="gray",vmin=0,vmax=5)
plt.colorbar()
cs=plt.contour(a2_vec,u2_vec,ll2/len(t),[0.7,1,2,3],colors="m")
plt.clabel(cs,[0.7,1,2,3],inline=True)
plt.xlabel(r"$u_2$ [m/2]")
plt.ylabel(r"$a_2$ [m/s$^2$]")
plt.title(r"Model 2: $\chi^2(u_2,a_2)/N$",fontsize=12)
plt.tight_layout()
plt.savefig("crash_ll2.png")
#plt.show()
plt.close()
e2 = 1/(33.0-15.0)*1/(5.0-0.0)*(u2_vec[1]-u2_vec[0])*(a2_vec[1]-a2_vec[0])*np.sum(np.exp(-ll2/2))
#
#
print ("Model 1: chi2-per-data = %f"%np.amin(ll1/len(t)))
print ("Model 2: chi2-per-data = %f"%np.amin(ll2/len(t)))
print ("Model 1: Evidence = %f"%e1)
print ("Model 2: Evidence = %f"%e2)
print ("Bayes factor = %f"%(e2/e1))
print ("Log Bayes factor = %f"%(np.log(e2/e1)))
#
#
# Data - fits
#
#plt.errorbar(x=t,y=s,yerr=sig,fmt="ko")
I = np.argmin(ll1)
fit1 = u1_vec[I]*t
print (u1_vec[I])
plt.errorbar(x=t,y=s-fit1,yerr=sig,fmt="bo",label="Model 1",alpha=0.5)
I = np.unravel_index(np.argmin(ll2),ll2.shape)
fit2 = u2_vec[I[0]]*t-0.5*a2_vec[I[1]]*t**2
print (u2_vec[I[0]],a2_vec[I[1]])
plt.errorbar(x=t,y=s-fit2,yerr=sig,fmt="ro",label="Model 2",alpha=0.5)
plt.axhline(1,color="k",ls="--")
plt.xlabel("Time [s]")
plt.ylabel("Residuals [m]")
plt.legend()
plt.tight_layout()
plt.savefig("crash_res.png")
#plt.show()
plt.close()

