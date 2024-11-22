import numpy as np
import matplotlib.pyplot as plt

tp = np.load("spind.npz")
nu = tp["nu"]
S = tp["S"]
sig = tp["err"]

# Brute force
avec = np.arange(-2,3,0.01)
Cvec = np.arange(0,2,0.005)
LL = np.zeros((len(avec),len(Cvec)))
for i in range(len(avec)):
   for j in range(len(Cvec)):
      LL[i,j] = -sig**-2*np.sum((S-(Cvec[j]*nu**avec[i]))**2)
LL-=np.amax(LL)

ext = [np.amin(Cvec),np.max(Cvec),np.amin(avec),np.amax(avec)]
plt.imshow(np.exp(LL),aspect="auto",origin="lower",extent=ext,cmap="cool")
plt.colorbar()
plt.xlabel(r"$C$[Jy]")
plt.ylabel(r"$\alpha$")
#
#
#Iterative via Newton's method
a = 2.9
C = 10.0
iiter=0
for i in range(10):
   b = np.array([np.sum(nu**a*(S+a*C*nu**a*np.log(nu))),np.sum(C*nu**a*np.log(nu)*(S+a*C*nu**a*np.log(nu)))])
   A = np.array([[np.sum(nu**(2*a)), np.sum(C*nu**(2*a)*np.log(nu))],[np.sum(C*nu**(2*a)*np.log(nu)), np.sum((C*nu**a*np.log(nu))**2)]])

   x = np.dot(np.linalg.inv(A),b)
   iiter+=1
   print("Iteration %d: C=%.4f, alpha=%.4f"%(iiter,x[0],x[1]))
   C,a=x
   plt.plot(C,a,'gx')

plt.title("Likelihood for spectral index fit",fontsize=12)
plt.tight_layout()
plt.savefig("spind_post.png")
plt.show()
plt.close()
