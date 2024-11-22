import numpy as np
import matplotlib.pyplot as plt
#
def pearson(x,y):
   n = len(x)
   pearson_r = (n*np.sum(x*y)-np.sum(x)*np.sum(y))/\
               ((n*np.sum(x**2)-(np.sum(x))**2)**0.5 *\
               (n*np.sum(y**2)-(np.sum(y))**2)**0.5)
   return pearson_r

tp = np.loadtxt("wd.txt",delimiter=",")

m = tp[:,0]
r = tp[:,1]
n = len(r)

msig = ((m*0.05)**2+0.03**2)**0.5
rsig = ((r*0.05)**2+0.003**2)**0.5

merr = np.random.randn(n)*msig
rerr = np.random.randn(n)*rsig

mm = m+merr
rm = r+rerr

f = open("wd_err.txt","w")
for i in range(len(m)):
   f.write("%f, %f\n"%(mm[i],rm[i])) 
f.close()

plt.errorbar(x=mm,y=rm,xerr=msig,yerr=rsig,fmt='k.')
plt.xlabel(r"Mass [M$_\odot$]")
plt.ylabel(r"Radius [R$_\odot$]")
plt.tight_layout()
plt.savefig("wd_mr.png")
#plt.show()
plt.close()
#
#
pearson_r = pearson(mm,rm)
print ("Pearsons coeff = ")
print (pearson_r)
exit(1)
#
#
Im = np.argsort(mm)
Ir = np.argsort(rm)
Rm = np.zeros(n)
Rr = np.zeros(n)
for i in range(n):
   Rm[Im[i]]=i+1
   Rr[Ir[i]]=i+1
#
spearman_r = pearson(Rm,Rr)
print ("Spearman coeff = ")
print (spearman_r)
