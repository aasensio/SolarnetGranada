import numpy as np
import matplotlib.pyplot as pl
import pymultinest
import seaborn as sn

lower = np.asarray([0.0, 0.0])
upper = np.asarray([50.0, 1.0])
result = 10.5
noise = 1.0

def Prior(cube, ndim, nparams):
	for  i in range(ndim):
		cube[i] = cube[i] * (upper[i] - lower[i]) + lower[i]

def loglike(cube, ndim, nparams, lnew):
	return -0.5*(result - cube[0]*cube[1])**2 / noise**2

pymultinest.run(loglike, Prior, 2, n_live_points=1000, resume=False, verbose=True)

a = pymultinest.Analyzer(n_params=2, outputfiles_basename='chains/1-')

samples = a.get_equal_weighted_posterior()

ind = np.arange(len(samples[:,0]))
ind = np.random.permutation(ind)
f, ax = pl.subplots(nrows=2, ncols=2, figsize=(10,10))
ax[0,0].plot(samples[ind,0])
ax[0,1].hist(samples[:,0], bins=20)

ax[1,0].plot(samples[ind,1])
ax[1,1].hist(samples[:,1], bins=20)

pl.tight_layout()
pl.savefig('samplesTwoNumbers.png')

f, ax = pl.subplots(figsize=(10,10))
ax.hexbin(samples[:,0], samples[:,1])
pl.savefig('2DTwoNumbers.png')