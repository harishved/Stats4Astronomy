import numpy as np
import matplotlib.pyplot as plt
#
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
Nb = 5000

tp = np.loadtxt("wd_err.txt",delimiter=",")
m = tp[:,0]
r = tp[:,1]
n = len(m)
#
samples_pearson = np.zeros(Nb)
samples_spearman = np.zeros(Nb)
#
mb = np.zeros(n)
rb = np.zeros(n)
#
for i in range(Nb):
   for j in range(n):
      I = np.ceil(np.random.rand()*(n-1)).astype(int)
      mb[j] = m[I]
      rb[j] = r[I]
   samples_pearson[i] = pearson(mb,rb)
   samples_spearman[i] = spearman(mb,rb)
#
#

y1,x1 = np.histogram(samples_pearson,bins=50)
x = 0.5*(x1[1:]+x1[:-1])
y = y1.astype(int)
plt.step(x=x,y=y,label="Pearson")
y1,x1 = np.histogram(samples_spearman,bins=50)
x = 0.5*(x1[1:]+x1[:-1])
y = y1.astype(int)
plt.step(x=x,y=y,label="Spearman")
plt.legend()
plt.xlabel("Coefficient")
plt.ylabel("Num. of occurances")
plt.tight_layout()
plt.savefig("wd_boot.png")
plt.show()
plt.close()
#
