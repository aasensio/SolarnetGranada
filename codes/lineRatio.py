import numpy as np
import matplotlib.pyplot as pl
import seaborn as sn
import pymilne
import scipy.integrate

# First line
lambda0 = 6302.5
JUp = 1.0
JLow = 1.0
gUp = 2.5
gLow = 0.0
lambdaStart = 6301.8
lambdaStep = 0.03
nLambda = 50
wavelength = lambdaStart + np.arange(nLambda) * lambdaStep

lineInfo = np.asarray([lambda0, JUp, JLow, gUp, gLow, lambdaStart, lambdaStep])

s = pymilne.milne(nLambda, lineInfo)

VMac = 0.0
damping = 0.04
B0 = 1.0
B1 = 5.0
mu = 1.0
VDop = 0.040
kl = 6.75

pV = np.exp(-(wavelength-lambda0-60e-3)**2 / 75e-3**2)

nB = 100
B = np.linspace(0.0,3500.0,nB)

SV1 = np.zeros((4,nB))
SV2 = np.zeros((4,nB))

pal = sn.color_palette()

thetas = [0, 30, 60, 85]
for j in range(4):
	for i in range(nB):
		modelSingle = np.asarray([B[i], thetas[j], 0.0, VMac, damping, B0, B1, VDop, kl])
		stokes = s.synth(modelSingle,mu)
		SV1[j,i] = scipy.integrate.simps(stokes[3,:] * pV, x=wavelength) / scipy.integrate.simps(stokes[0,:] * pV, x=wavelength)
        
# Second line
lambda0 = 6301.5
JUp = 1.0
JLow = 1.0
gUp = 1.5
gLow = 0.0
lambdaStart = 6300.8
lambdaStep = 0.03
nLambda = 50
wavelength = lambdaStart + np.arange(nLambda) * lambdaStep

lineInfo = np.asarray([lambda0, JUp, JLow, gUp, gLow, lambdaStart, lambdaStep])

s = pymilne.milne(nLambda, lineInfo)
pV = np.exp(-(wavelength-lambda0-60e-3)**2 / 75e-3**2)
thetas = [0, 30, 60, 85]
for j in range(4):
	for i in range(nB):
		modelSingle = np.asarray([B[i], thetas[j], 0.0, VMac, damping, B0, B1, VDop, kl])
		stokes = s.synth(modelSingle,mu)
		SV2[j,i] = scipy.integrate.simps(stokes[3,:] * pV, x=wavelength) / scipy.integrate.simps(stokes[0,:] * pV, x=wavelength)
        
pl.close('all')
f, ax = pl.subplots()
for i in range(4):
	ax.plot(B, SV1[i,:] / SV2[i,:], color=pal[i], label=r'$\theta_B$={0}'.format(thetas[i]))
ax.set_xlabel('B [G]')
ax.set_ylabel('Line ratio')
ax.axhline(2.5/1.5, color=pal[4])
pl.legend(loc='lower left')
pl.savefig('lineRatio.pdf')
pl.savefig('lineRatio.png')