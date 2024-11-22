import numpy as np
import matplotlib.pyplot as plt
#
def pearson(x,y):
   n = len(x)
   pearson_r = (n*np.sum(x*y)-np.sum(x)*np.sum(y))/\
               ((n*np.sum(x**2)-(np.sum(x))**2)**0.5 *\
               (n*np.sum(y**2)-(np.sum(y))**2)**0.5)
   return pearson_r
#
def spearman(x,y):
   Im = np.argsort(x)
   Ir = np.argsort(y)
   Rm = np.zeros(n)
   Rr = np.zeros(n)
   for i in range(n):
      Rm[Im[i]]=i+1
      Rr[Ir[i]]=i+1
   #
   spearman_r = pearson(Rm,Rr)
   return spearman_r
#
#
tp = np.loadtxt("wd_err.txt",delimiter=",")

m = tp[:,0]
r = tp[:,1]
n = len(r)
ntest = 1000

actual_coeff = spearman(m,r)

coeffs = np.zeros(ntest)
for i in range(ntest):
   np.random.shuffle(m)
   coeffs[i] = spearman(m,r)

y1,x1 = np.histogram(coeffs,bins=50)
x = 0.5*(x1[1:]+x1[:-1])
y = y1.astype(float)

plt.step(x,y,color="k")
plt.axvline(x=actual_coeff,color="m")
plt.xlim([-1,1])
plt.xlabel("Spearman's coefficient")
plt.ylabel("Number of occurances")
plt.tight_layout()
plt.savefig("ht.png")
plt.show()
plt.close()
