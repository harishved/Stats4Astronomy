import numpy as np
import matplotlib.pyplot as plt
N = 10000

y = np.random.randn(N)*2.5

plt.hist(y,bins=50)
plt.xlabel("v [km/hr]")
plt.ylabel("Number of occurances")
plt.title("%d trials"%N,fontsize=12)
plt.tight_layout()
plt.savefig("gauss.png")
plt.show()
plt.close()

print ("Mean = %f"%np.mean(y))
print ("STD = %f"%np.std(y))

E = 0.5*y**2

plt.hist(E,bins=50)
plt.xlabel(r"Energy [$10^3$kg km/s]")
plt.ylabel("Number of occurances")
plt.title("%d trials"%N,fontsize=12)
plt.tight_layout()
plt.savefig("energy.png")
plt.show()
plt.close()
