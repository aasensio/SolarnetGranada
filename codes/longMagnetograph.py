import numpy as np
import matplotlib.pyplot as pl
import seaborn as sn
import pymilne
import scipy.integrate


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

BField = 100.0
BTheta = 0.0
BChi = 0.0
VMac = 0.0
damping = 0.04
B0 = 1.0
B1 = 5.0
mu = 1.0
VDop = 0.040
kl = 6.75

pV = np.exp(-(wavelength-lambda0-60e-3)**2 / 75e-3**2)
pQ = np.exp(-(wavelength-lambda0-120e-3)**2 / 75e-3**2)

nB = 100
B = np.linspace(0.0,3500.0,nB)

Bpar = np.zeros((2,4,nB))
Bperp = np.zeros((4,nB))
SV = np.zeros((2,4,nB))
SQ = np.zeros((4,nB))

pal = sn.color_palette()

thetas = [0, 30, 60, 85]

for j in range(4):
	for i in range(nB):
		modelSingle = np.asarray([B[i], thetas[j], 0.0, VMac, damping, B0, B1, VDop, kl])
		stokes = s.synth(modelSingle,mu)
		Bpar[0,j,i] = B[i] * np.cos(thetas[j]*np.pi/180.0)
		Bperp[j,i] = B[i] * np.sin(thetas[j]*np.pi/180.0)
		SV[0,j,i] = scipy.integrate.simps(stokes[3,:] * pV, x=wavelength) / scipy.integrate.simps(stokes[0,:] * pV, x=wavelength)
		SQ[j,i] = -scipy.integrate.simps(stokes[1,:] * pQ, x=wavelength) / scipy.integrate.simps(stokes[0,:] * pQ, x=wavelength)
		
		modelSingle = np.asarray([B[i], 180.0-thetas[j], 0.0, VMac, damping, B0, B1, VDop, kl])
		stokes = s.synth(modelSingle,mu)
		Bpar[1,j,i] = B[i] * np.cos((180.0-thetas[j])*np.pi/180.0)
		SV[1,j,i] = scipy.integrate.simps(stokes[3,:] * pV, x=wavelength) / scipy.integrate.simps(stokes[0,:] * pV, x=wavelength)		

pl.close('all')
f, ax = pl.subplots()
for j in range(4):
	ax.plot(Bpar[0,j,:], SV[0,j,:], color=pal[j], label=r'$\theta_B=${0}'.format(thetas[j]))
	ax.plot(Bpar[1,j,:], SV[1,j,:], color=pal[j])
	
ax.set_xlabel('B$_\parallel$')
ax.set_ylabel('S$_V$')
ax.set_xlim([-3500,3500])
pl.legend()
pl.savefig('SV_vs_B.pdf')
pl.savefig('SV_vs_B.png')

f, ax = pl.subplots()
for j in range(4):
	ax.plot(Bperp[j,:], SQ[j,:], color=pal[j], label=r'$\theta_B=${0}'.format(thetas[j]))	
	
ax.set_xlabel('B$_\perp$')
ax.set_ylabel('S$_Q$')
ax.set_xlim([0,3500])
pl.legend(loc='upper left')
pl.savefig('SQ_vs_B.pdf')
pl.savefig('SQ_vs_B.png')