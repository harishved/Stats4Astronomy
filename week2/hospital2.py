import numpy as np
import matplotlib.pyplot as plt

b_old = 0.87
n_vol = 10
b = np.linspace(0,1,1000)
db = b[1]-b[0]

posterior = np.zeros(b.shape)
prior = np.ones(b.shape)
likelihood = b**n_vol
evidence = np.sum(prior*likelihood)*db
posterior = likelihood*prior/evidence

plt.plot(b,posterior,'k',linewidth=1.5)
plt.xlabel("Chance of success")
plt.ylabel("Probability density")

I = np.argmin(np.absolute(b-b_old))
tp = db*np.sum(posterior[I:])
print ("Prob of bias > old value = %f"%tp)

plt.axvline(b_old)
plt.fill_between(x=b[I:],y1=np.zeros(len(b[I:])),y2=posterior[I:],color="cyan",alpha=0.7)
plt.tight_layout()
plt.savefig("hospital.png")
plt.show()
plt.close()
