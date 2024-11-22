import numpy as np
nmc = 100000
N = 30
yes=0
for i in range(nmc):
   bdays = np.ceil(np.random.rand(N)*365).astype(int)
   unique_bdays = list(set(bdays))
   if len(unique_bdays)<N:
      yes+=1

print (yes/nmc)
   
