# Statistics for Astronomy: Chapter 3
# Author: Harish Vedantham
# Gull's light=house problem
#
import numpy as np
import matplotlib.pyplot as plt

npulse  = [1,2,3,4,8,16,32,64,128]
beta = 1
alpha_real = 0
alpha_vec = np.arange(-5,5,0.01)
iplot=1

plt.figure(figsize=(6,6))

for n in npulse:
   theta = np.random.rand(n)*np.pi - np.pi/2
   x = np.tan(theta)
   logpdf = np.zeros(alpha_vec.shape)
   for i in range(n):
      logpdf+=np.log(beta/np.pi/(beta**2 + (x[i]-alpha_vec)**2))
   ax = plt.subplot(3,3,iplot) 
   y = np.exp(logpdf)
   ax.plot(alpha_vec,y)
   ax.set_yticklabels([])
   iplot+=1
   ax.set_xlabel(r"$\alpha$")
   ax.set_ylabel(r"${\rm prob}(\alpha|x)$")
   ax.set_title(r"$n=%d$"%n)
#   for k in range(n):
#      if n<=3:
#         ax.plot(x[k],np.amax(y)*0.9,'kx')
#   ax.set_xlim([-5,5])

plt.tight_layout()
plt.savefig("lighthouse.png")
plt.show()
plt.close()
