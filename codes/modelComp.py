import numpy as np
import pymultinest
import os

# Create the directory where the Markov chains will be saved
if not os.path.exists("chains"): 
	os.mkdir("chains")

# Set the number of parameters of your model and their ranges
# Also set the independent variable and the uncertainty standard deviation
nParameters = 3
t = np.linspace(0.0, 20, 30)         # x
y = np.ones(30)                      # measured values
error = np.ones(30) * 0.01           # noise
lower = np.asarray([0.0, 0.0, 0.0])
upper = np.asarray([1.0, 1.0, 1.0])

def model(params):
	"""
	Returns the model that will be used for fitting
	
	Args:
	    params (float): parameters of the model
	
	Returns:
	    TYPE: model
	"""
	return params[0] * t + params[1]
	

def Prior(cube, ndim, nparams):
	"""
	Transform from the unit hypercube to the range of parameters
	
	Args:
	    cube (float): positions on the unit hypercube
	    ndim (int): number of dimensions
	    nparams (int): number of parameters
	
	Returns:
	    float: the transformed hypercube
	"""
	for  i in range(ndim):
		cube[i] = cube[i] * (upper[i] - lower[i]) + lower[i]

def loglike(cube, ndim, nparams, lnew):
	"""
	Returns the log-likelihood
	
	Args:
	    cube (TYPE): variables
	    ndim (TYPE): number of dimensions
	    nparams (TYPE): number of parameters
	    lnew (TYPE): log-likelihood
	
	Returns:
	    TYPE: return the log-likelihood
	"""
	return -0.5*(y - model(cube))**2 / error**2

# Initialize the pyMultinest package
pymultinest.run(loglike, Prior, nParameters, resume=False, verbose=True)

# Read the output
out = pymultinest.Analyzer(n_params=2, outputfiles_basename='chains/1-')

logEvidence = out.get_stats()['nested importance sampling global log-evidence']
logEvidenceError = out.get_stats()['nested importance sampling global log-evidence error']

print "log Z={0} +- {1}".format(logEvidence, logEvidenceError)