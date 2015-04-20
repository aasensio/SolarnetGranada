import numpy as np
import matplotlib.pyplot as pl
import seaborn as sn
import pymilne
import scipy.integrate


lambda0 = 5250.21
JUp = 0.0
JLow = 1.0
gUp = 0.0
gLow = 3.0
lambdaStart = 5249.5
lambdaStep = 0.015
nLambda = 100
wavelength = lambdaStart + np.arange(nLambda) * lambdaStep

lineInfo = np.asarray([lambda0, JUp, JLow, gUp, gLow, lambdaStart, lambdaStep])

s = pymilne.milne(nLambda, lineInfo)

BField = 100.0
BTheta = 0.0
BChi = 0.0
VMac = 0.0
damping = 0.04
B0 = 1.0
B1 = 12.0
mu = 1.0
VDop = 0.032
kl = 6.1

nB = 100
B = np.linspace(0.0,3500.0,nB)

Bpar = np.zeros((4,nB))
BEstimated = np.zeros((4,nB))

pal = sn.color_palette()

thetas = [15, 30, 60, 75]

for j in range(4):
	for i in range(nB):
		modelSingle = np.asarray([B[i], thetas[j], 0.0, VMac, damping, B0, B1, VDop, kl])
		stokes = s.synth(modelSingle,mu)
		
		Ic = stokes[0,0]
		
		Iplus = 0.5*(stokes[0,:] + stokes[3,:])
		Iminus = 0.5*(stokes[0,:] - stokes[3,:])
		
		lambdaPlus = scipy.integrate.simps((0.5*Ic - Iplus) * wavelength, x=wavelength) / scipy.integrate.simps((0.5*Ic - Iplus), x=wavelength)
		lambdaMinus = scipy.integrate.simps((0.5*Ic - Iminus) * wavelength, x=wavelength) / scipy.integrate.simps((0.5*Ic - Iminus), x=wavelength)
		
		BEstimated[j,i] = 1.071e9 / (3.0 * 5250.21**2) * (lambdaPlus-lambdaMinus)*1e3
		Bpar[j,i] = B[i] * np.cos(thetas[j]*np.pi/180.0)		

pl.close('all')
f, ax = pl.subplots()
for j in range(4):
	ax.plot(Bpar[j,:], (BEstimated[j,:]-Bpar[j,:]) / Bpar[j,:], color=pal[j], label=r'$\theta_B=${0}'.format(thetas[j]))	
	
ax.set_xlabel('B$_\parallel$')
ax.set_ylabel('Relative error')
ax.set_xlim([0,3500])
pl.legend()
pl.savefig('cog_vs_B.pdf')
pl.savefig('cog_vs_B.png')