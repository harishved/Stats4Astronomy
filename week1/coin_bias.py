# Statistics for Astronomy: Chapter 1
# 
from math import factorial as fac
import numpy as np
import matplotlib.pyplot as plt
#
nroll = 100 # Number of tosses
ntail = 63 # Number of tails

b = np.linspace(0,1,1000) # Vector of bias valyes
db = b[1]-b[0] # increment (needed for integration)

prior = np.ones(b.shape) # Prior on b
likelihood = np.zeros(b.shape) # Initialize likelihood vector

ncr = fac(nroll)/fac(ntail)/fac(nroll-ntail) # NCr

for i in range(len(b)):
   likelihood[i] = ncr*b[i]**ntail*(1-b[i])**(nroll-ntail)

evidence = db*np.sum(likelihood*prior)

posterior = prior*likelihood/evidence
#
# Plot the posterior
plt.plot(b,posterior)
plt.xlabel(r"$b$")
plt.ylabel(r"Prob$(b|E)$")
plt.title("E: %d tails in %d tosses"%(ntail,nroll),fontsize=12)
plt.tight_layout()
plt.savefig("bias.png")
plt.close()
#
# Calc. Prob of bias towards tails
I = np.where(b>0.5)[0]
print ("Prob b>0.5 is %f"%(db*np.sum(posterior[I])))
#
# Most likely value of bias
I = np.argmax(posterior)
print ("Most likely value of b is %f"%b[I])
# 
# Expected value of bias
expec = db*np.sum(posterior*b)
print ("Expected value is %f"%expec)
#
# Standard deviation of bias
std = (db*np.sum(posterior*(b-expec)**2))
print ("Standard dev is %f"%std)
#
# Calculate the two-sided 99% credible interval for the bias
area = 0
i=0
while(area<0.99):
   area = db*np.sum(posterior[I-i:I+i+1]) # Integrate over a region around the peak value
   i+=1
print ("99 per-cent interval is %f to %f"%(b[I-i],b[I+i]))
