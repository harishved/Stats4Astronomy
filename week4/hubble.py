import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm as sqrtm

N = 15
H = 500.0
err = 150

d = np.random.rand(N)*2
v = H*d + np.random.randn(N)*err

plt.errorbar(x=d,y=v,yerr=err,fmt="ko")
plt.xlabel(r"$d\,[{\rm Mpc}]$")
plt.ylabel(r"$v\,[{\rm km/s}]$")
plt.title("Mock data to derive Hubble's relationship")
plt.savefig("hubble_data.png")
plt.show()
plt.close()

np.savez("hubble_data.npz",d=d,v=v,H=H,err=err)

# MAX LIKELIHOOD VALUE
A = np.array([[np.sum(d**2), np.sum(d)],[np.sum(d), N]])
b = np.array([np.sum(v*d), np.sum(v)])
mll = np.dot(np.linalg.inv(A),b)
print (mll)
# MODEL FITTING
# 
A = np.sum(d**2)/err**2
D = N/err**2
C = np.sum(d)/err**2

B = np.array([[A,C],[C,D]])
Binv = np.linalg.inv(B)
covmat = sqrtm(Binv)
#
# BRUTE FORCE
Hvec = np.arange(200.0,900.0,10.0)
Cvec = np.arange(-500.0,500.0,10.0)
ll = np.zeros((len(Hvec),len(Cvec)))
for i in range(len(Hvec)):
   for j in range(len(Cvec)):
      ll[i,j] = -np.sum((v-Hvec[i]*d-Cvec[j])**2/2/err**2)

#
ll-=np.amax(ll)
ell = np.exp(ll)

ext = [np.amin(Cvec),np.amax(Cvec),np.amin(Hvec),np.amax(Hvec)]
plt.imshow(ell,aspect="auto",origin="lower",extent=ext)
plt.plot(mll[1],mll[0],'mo',ms=5)
plt.colorbar()
plt.xlabel(r"$C$ [km/s]")
plt.ylabel(r"$H$ [km/s/Mpc]")


eigval,eigvec = np.linalg.eig(covmat)
bmaj = eigval[0]
bmin = eigval[1]
#major axis
x1 = mll[1]
x2 = x1+2*bmin*eigvec[0,0]
y1 = mll[0]
y2 = y1 + 2*bmin*eigvec[0,1]
plt.plot([x1,x2],[y1,y2],'m',linewidth=2,alpha=0.7)
x2= x1-2*bmin*eigvec[0,0]
y2 = y1-2*bmin*eigvec[0,1]
plt.plot([x1,x2],[y1,y2],'m',linewidth=2,alpha=0.7)

x1 = mll[1]
x2 = x1+2*bmaj*eigvec[1,0]
y1 = mll[0]
y2 = y1 + 2*bmaj*eigvec[1,1]
plt.plot([x1,x2],[y1,y2],'m',linewidth=2,alpha=0.7)
x2= x1-2*bmaj*eigvec[1,0]
y2 = y1-2*bmaj*eigvec[1,1]
plt.plot([x1,x2],[y1,y2],'m',linewidth=2,alpha=0.7)



plt.tight_layout()
plt.savefig("hubble_post.png")
plt.show()
plt.close()


# MARGINALIZATION
dC = Cvec[1]-Cvec[0]
pdfH = dC*np.sum(ell,axis=1)
pdfH/=np.sum(pdfH)*(Hvec[1]-Hvec[0])
plt.plot(Hvec,pdfH)
plt.xlabel(r"$H$ [km/s/Mpc]")
plt.ylabel(r"prob$(H)$ [Mpc s / km]")
plt.axvline(mll[0])
plt.tight_layout()
plt.savefig("hubble_post_mar.png")
plt.show()
plt.close()




