import numpy as np
import matplotlib.pyplot as plt
import corner
#
#
tp = np.load("rv.npz")
A = tp["A"]
sig = tp["err"]
t = tp["t"]
rv = tp["rv"]
per = tp["per"]

Nmc = int(1e6)


samples=[]
x=[0.5,0.5,0.5]
ll = -0.5*sig**-2*np.sum((rv-x[0]*np.cos(2*np.pi*x[1]*t+x[2]))**2)

for i in range(1,Nmc):
   #xprop = [np.random.rand()+0.4, np.random.rand()*1.5+0.2, np.random.rand()*2*np.pi]
   xprop = [x[0]+np.random.randn()*0.1,\
            x[1]+np.random.randn()*0.1,\
            x[2]+np.random.randn()*0.1]
   newll = -0.5*sig**-2*np.sum((rv-xprop[0]*np.cos(2*np.pi*xprop[1]*t+xprop[2]))**2)
   u = np.random.rand()
   if u<min(1,np.exp(newll-ll)):
      print ("Accept: "+str(xprop)) 
      samples.append(xprop)
      ll = newll
      x=xprop
   else:
      samples.append(x)
      print ("Reject: "+str(xprop)) 
#
#
x = np.array(samples)[1000:,:]
np.savez("samples.npz",x=x)
plt.figure(figsize=(6,6))
plt.subplot(311)
plt.plot(x[:,0],'k',linewidth=0.5)
plt.ylabel(r"$A$ [m/s]")
plt.subplot(312)
plt.plot(x[:,1],'k',linewidth=0.5)
plt.ylabel(r"$P\,[{\rm yr}^{-1}]$")
plt.subplot(313)
plt.plot(x[:,2],'k',linewidth=0.5)
plt.ylabel(r"$\phi$ [rad]")
plt.xlabel(r"Iteration")
plt.tight_layout()
plt.savefig("rv_mc_samples_full.png")
plt.show()
plt.close()
#
#
print (np.mean(x,axis=1))
print (np.std(x,axis=1))
#
#
fig, axs = plt.subplots(1,1)
figure = corner.corner(\
    x,\
    labels=[\
        r"$A\,[{\rm m/s}]$",\
        r"$P\,[{\rm yr}^{-1}]$",\
        r"$\phi\,[{\rm rad}]$",\
    ],\
    quantiles=[0.16, 0.5, 0.84],\
    show_titles=True,\
    title_kwargs={"fontsize": 12},
)
plt.savefig("rv_corner.png")
plt.close()
