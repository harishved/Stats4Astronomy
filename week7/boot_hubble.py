import numpy as np
import matplotlib.pyplot as plt
import corner
#
tp = np.load("hubble_data.npz")
v = tp["v"]
d = tp["d"]
n = len(v)
Nb = 2000
#
samples = np.zeros((Nb,2))
db = np.zeros(n)
vb = np.zeros(n)

for i in range(Nb):
   # MAX LIKELIHOOD VALUE
   for j in range(n):
      I = np.floor(np.random.rand()*(n-1)).astype(int)
      db[j] = d[I]
      vb[j] = v[I]

   A = np.array([[np.sum(db**2), np.sum(db)],[np.sum(db), n]])
   b = np.array([np.sum(vb*db), np.sum(vb)])
   mll = np.dot(np.linalg.inv(A),b)
   samples[i,0] = mll[0]
   samples[i,1] = mll[1]
#
#
fig, axs = plt.subplots(1,1)
figure = corner.corner(\
    samples,\
    labels=[\
        r"$H$",\
        r"$C$"\
    ],\
    quantiles=[0.16, 0.5, 0.84],\
    show_titles=True,\
    title_kwargs={"fontsize": 12},\
    title_fmt='.3f'\
)
plt.savefig("boot_spec_corner.png")
plt.close()

