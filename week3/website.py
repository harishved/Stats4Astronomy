import numpy as np
import matplotlib.pyplot as plt

hits = np.random.poisson(lam=100.0,size=100)
plt.hist(hits,bins=10)
plt.xlabel("Number of website visits")
plt.ylabel("Number of occurances")
plt.tight_layout()
plt.savefig("website.png")
plt.show()
plt.close()
