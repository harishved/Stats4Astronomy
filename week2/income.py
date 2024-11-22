import numpy as np
import matplotlib.pyplot as plt

g = 10.0
sig = 1.0
mu = 1.5

x = np.arange(g,100*g,0.01*g)
y = (2*np.pi*sig**2)**-0.5 * \
    np.exp(-(np.log(x-g)-mu)**2/2/sig**2)
#    (x-g)**-1
y/=(x[1]-x[0])*np.sum(y)

plt.plot(x,y)
plt.xlabel("Income in kiloeuros")
plt.ylabel("Probability density")
plt.xlim([g,10*g])


# Most likely value
I = np.argmax(y)
print ("Most likely value = %f"%x[I])
plt.axvline(x[I],c="0.3",ls="--")
plt.text(x=x[I]*1.02,y=np.amax(y)/2,s="Most likely",rotation=90,c="0.2")

# Expected value
expec =  ((x[1]-x[0])*np.sum(x*y))
print ("Expected value = %f"%expec)
plt.axvline(expec,c="0.3",ls="--")
plt.text(x=expec*1.02,y=np.amax(y)/2,s="Expected value",rotation=90,c="0.3")

# Median value
area = 0
i=0
while (area<0.5):
   area = (x[1]-x[0])*np.sum(y[:i])
   i+=1
med =  (x[i])
print ("Median value = %f"%med)
plt.axvline(med,c="0.3",ls="--")
plt.text(x=med*1.02,y=np.amax(y)/2,s="Median value",rotation=90,c="0.2")

plt.title("Hypothetical income distribution function",fontsize=12)
plt.tight_layout()
plt.savefig("income.png")
plt.show()
plt.close()
