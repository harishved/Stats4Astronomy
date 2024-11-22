import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fac

wavelength = np.arange(6560-100,6560+100,1.0)
background = 10
signal = 12
width = 2.0

exp_signal = background + signal*np.exp(-(wavelength-6560)**2/2/width**2)

data = np.zeros(exp_signal.shape)
for i in range(len(data)):
   data[i] = np.random.poisson(lam=exp_signal[i])
plt.figure(figsize=(8,3))
plt.step(wavelength,data)

plt.xlabel("Wavelength in Angstrom")
plt.ylabel("Photon counts")
plt.savefig("aurora.png")
plt.show()
plt.close()

# POSTERIOR
la = np.arange(0.1,30,0.1)
lb = np.arange(0.1,30,0.1)
log_post = np.zeros((len(la),len(lb)))

for i in range(len(la)):
   for j in range(len(lb)):
      l = lb[j] + la[i]*np.exp(-(wavelength-6560)**2/2/width**2)
      log_post[i,j] = np.sum(-l+data*np.log(l))

ext=[np.amin(lb),np.amax(lb),np.amin(la),np.amax(la)]
log_post-=np.amax(log_post)
I = np.unravel_index(np.argmax(log_post),log_post.shape)
print (I)
print (la[I[0]],lb[I[1]])
post = np.exp(log_post)

plt.imshow(post,origin="lower",aspect="auto",extent=ext)
plt.xlabel(r"$\lambda_b$")
plt.ylabel(r"$\lambda_a$")
plt.title(r"${\rm prob}(\lambda_a,\lambda_b|N_1,N_2..)$")
plt.colorbar()
plt.tight_layout()
plt.savefig("aurora_post.png")
plt.show()
plt.close()

# MARGINALIZATION

dlb = lb[1]-lb[0]
post_la = np.zeros(la.shape)
for i in range(len(la)):
   post_la[i] = dlb*np.sum(post[i,:])
dla = la[1]-la[0]
post_la/=dla*np.sum(post_la)

plt.plot(la,post_la)
plt.xlabel(r"$\lambda_a$")
plt.ylabel(r"${\rm prob}(\lambda_a|N_1,N_2...)$")
plt.title("Marginalized posterior",fontsize=12)
plt.tight_layout()
plt.savefig("aurora_posta.png")
plt.show()
plt.close()

# POINT ESTIMATES
mu = dla*np.sum(la*post_la)
sig = (dla*np.sum((la-mu)**2*post_la))**0.5
maxl = la[np.argmax(post_la)]
print (mu,sig,maxl)



