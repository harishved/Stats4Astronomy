# Statistics for Astronomy: Chapter 6
# Author: Harish Vedantham
#
import numpy as np
import matplotlib.pyplot as plt
import corner
#
'''
locs = [550,551] # Real locations of the lines
sig = 0.005   # Standard deviation of the noise
amps = [0.1,0.05] # Peak oprtical depth of the lines
#
# GENERATE DATA
f = np.arange(540,560,0.2)
spec = np.ones(len(f))
for i in range(len(locs)):
   spec-=amps[i]/(1+(f-locs[i])**2)
spec+=np.random.randn(len(f))*sig
# 
#Save data 
np.savez("spec.npz",sig=sig,locs=locs,amps=amps,f=f,spec=spec)
exit(1)
'''
tp = np.load("spec.npz")
sig=tp["sig"]
locs = tp["locs"]
amps = tp["amps"]
f = tp["f"]
spec = tp["spec"]
#
#
# Plot the data with error bars
#
plt.figure(figsize=(5,2.5))
plt.errorbar(x=f,y=spec,yerr=sig,fmt="k.")
plt.xlabel("Frequency [arb. units]")
plt.ylabel("Amplitude [arb. units]")
plt.axhline(y=1,color="0.7")
plt.title("Mock spectrum",fontsize=10)
plt.tight_layout()
plt.savefig("spec_data.png")
plt.show()
plt.close()
#
#
# SINGLE COMPONENT MODEL
# Monte Carlo iterations
#
Nmc = 400000 # Number of Monte Carlo runs
A0 = 1-np.amin(spec) # Initial guess
mu0 = f[np.argmin(spec)] # Initial line centre
x = [A0,mu0] # Parameter vector
oldll = -np.sum((spec-1+A0/((f-mu0)**2+1))**2)/2/sig**2 # Starting log likelihood
samples = [] # Monte Carlo samples
peak_ll_1=-1e9 # Starting value for the peak likelihood
#
for i in range(Nmc):
   newx = [x[0]+np.random.randn()*0.05,x[1]+np.random.randn()*0.05] # Proposal
   newll = -np.sum((spec-1+newx[0]/((f-newx[1])**2+1))**2)/2/sig**2 # New likelihood ap proposal
   if newll>peak_ll_1:
      peak_ll_1 = newll # Update peak likelihood
      peak_x1 = newx
   if newll>oldll: # Monte Carlo decision
      samples.append(newx)
      x = newx
      oldll = newll
   else:
      u = np.random.rand()
      if u<np.exp(newll-oldll):
         samples.append(newx)
         x = newx
         oldll = newll
      else:
         samples.append(x)
#
#
x = np.array(samples)[100:,:] # After the Burn in
# Print results for Model 1
np.set_printoptions(precision=4)
print ("Model 1")
print ("Mean values = ")
x1_mean = np.mean(x,axis=0)
print(x1_mean)
print ("max likelihood value = ")
print (np.array(peak_x1))
print ("Covariance matrix = ")
cov1 = np.cov(np.transpose(x)) # Covariance matrix for Model 1
print (cov1)
print ("Chi2 = ")
print (-2*peak_ll_1)

# Calculate log evidence for Model 1
log_evidence1 = -np.log(560-540)-np.log(1-0)\
                +len(x[0,:])*0.5*np.log(2*np.pi)+\
                0.5*np.log(np.linalg.det(cov1))+peak_ll_1
print ("log evidence = %f"%log_evidence1)
# Corner plot for Model 1
fig, axs = plt.subplots(1,1)
figure = corner.corner(\
    x,\
    labels=[\
        r"$\tau$",\
        r"$\mu$"\
    ],\
    quantiles=[0.16, 0.5, 0.84],\
    show_titles=True,\
    title_kwargs={"fontsize": 12},\
    title_fmt='.3f'\
)
plt.savefig("spec_1_corner.png")
plt.close()
#
# 2 component model
# Same steps as before but with a new component
#
Nmc = 1000000
A0 = (1-np.amin(spec))/2
mu0 = f[np.argmin(spec)]-2
A1 = (1-np.amin(spec))/2
mu1 = f[np.argmin(spec)]+2
#
x = [A0,mu0,A1,mu1]
oldll = -np.sum((spec-1+A0/((f-mu0)**2+1)+A1/((f-mu1)**2+1))**2)/2/sig**2
samples = []
peak_ll_2 = -1e9
for i in range(Nmc):
   newx = [x[0]+np.random.randn()*0.02,x[1]+np.random.randn()*0.02,\
            x[2]+np.random.randn()*0.02,x[3]+np.random.randn()*0.02]
   newll = -np.sum((spec-1+newx[0]/((f-newx[1])**2+1)+newx[2]/((f-newx[3])**2+1))**2)/2/sig**2
   if newll>peak_ll_2:
      peak_ll_2 = newll
      peak_x2 = newx
   if newll>oldll:
      samples.append(newx)
      x = newx
      oldll = newll
   else:
      u = np.random.rand()
      if u<np.exp(newll-oldll):
         samples.append(newx)
         x = newx
         oldll = newll
      else:
         samples.append(x)

x = np.array(samples)[20000:,:]
print ("Model 2")
print ("Mean values = ")
x2_mean = np.mean(x,axis=0)
print (x2_mean)
print ("Max likelihood values = ")
print (np.array(peak_x2))
print ("Covariance matrix = ")
cov2 = np.cov(np.transpose(x))
print (cov2)
print ("Chi2 = ")
print (-2*peak_ll_2)

log_evidence2 = -2*np.log(560-540)-2*np.log(1-0)\
                +len(x[0,:])*0.5*np.log(2*np.pi)+\
                0.5*np.log(np.linalg.det(cov2))+peak_ll_2
print ("log evidence = %f"%log_evidence2)
#
#
fig, axs = plt.subplots(1,1)
figure = corner.corner(\
    x,\
    labels=[\
        r"$\tau_1$",\
        r"$\mu_1$",\
        r"$\tau_2$",\
        r"$\mu_2$"\
    ],\
    quantiles=[0.16, 0.5, 0.84],\
    show_titles=True,\
    title_kwargs={"fontsize": 12},\
    title_fmt='.3f'\
)
plt.savefig("spec_2_corner.png")
plt.close()
#
#
# PLot the residuals
fit1 = 1-x1_mean[0]/((f-x1_mean[1])**2+1)
fit2 = 1-x2_mean[0]/((f-x2_mean[1])**2+1) - x2_mean[2]/((f-x2_mean[3])**2+1)
plt.figure(figsize=(5,2.5))
plt.errorbar(x=f,y=spec-fit1,yerr=sig,fmt="m.",label=r"$M1$")
plt.errorbar(x=f,y=spec-fit2,yerr=sig,fmt="b.",label=r"$M2$")
plt.ylabel("Residual [arb. units]")
plt.xlabel("Freuqency [arb. units]")
plt.legend()
plt.tight_layout()
plt.savefig("spec_residual.png")
plt.close()
