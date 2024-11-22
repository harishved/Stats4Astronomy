import numpy as np
import matplotlib.pyplot as plt

tp = np.load("rv.npz")
A = tp["A"]
sig = tp["err"]
t = tp["t"]
rv = tp["rv"]
per = tp["per"]

Nmc = int(1e6)

x=np.zeros(Nmc+1)
x[0]=0.2
ll = -0.5*sig**-2*np.sum((rv-np.cos(2*np.pi*x[0]*t))**2)
for i in range(1,Nmc):
   xprop = np.random.rand()+0.4
   #xprop = x[i-1]+np.random.randn()*0.1
   newll = -0.5*sig**-2*np.sum((rv-np.cos(2*np.pi*xprop*t))**2)
   u = np.random.rand()
   if u<min(1,np.exp(newll-ll)):
      print ("Accept: %f, %f, %f"%(xprop,ll,newll))
      x[i] = xprop
      ll = newll
   else:
      x[i] = x[i-1]
      #print ("Reject: %f, %f, %f"%(xprop,ll,newll))

plt.figure(figsize=(6,3))
plt.subplot(121)
plt.plot(x[:100],'k')
plt.ylabel("Monte-Carlo values")
plt.xlabel("Iteration")
plt.subplot(122)
plt.plot(x[100:-1],'k',linewidth=0.1)
plt.xlabel("Iteration")
plt.tight_layout()
plt.savefig("rv_mc_values.png")
plt.show()
plt.close();
x=x[100:-1]

y1,x1 = np.histogram(x,bins=40)
xvec = 0.5*(x1[1:]+x1[:-1])
y = y1.astype(float)
dx = xvec[1]-xvec[0]
y/=dx*np.sum(y)
# Brute force calculation
log_post = np.zeros(xvec.shape)
for i in range(len(log_post)):
   log_post[i] = -0.5*sig**-2*np.sum((rv-np.cos(2*np.pi*xvec[i]*t))**2)
log_post-=np.amax(log_post)
post = np.exp(log_post)
post/=dx*np.sum(post)

plt.step(xvec,y,label="Metropolis-Hastings")
plt.plot(xvec,post,label="Brute-force")
plt.legend()
#plt.xlim([0.4,1.4])
plt.xlabel("Orbital freuqency [1/year]")
plt.ylabel("Posterior density function")
plt.title(r"$N = 10^{%d}$"%np.log10(Nmc))
#plt.yscale("log")
plt.tight_layout()
plt.savefig("rv_mh.png")
plt.show()
plt.close()
