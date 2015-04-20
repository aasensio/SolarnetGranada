import numpy as np
import matplotlib.pyplot as pl
import seaborn as sn

thetaReal = np.linspace(0.0,180.0,200)
x = np.asarray([1.0,0.1,0.01])
f, ax = pl.subplots()
tanTheta = np.tan(thetaReal*np.pi/180.0)
ind = np.where(tanTheta < 0.0)
for i in range(3):
    out = np.arctan2(tanTheta, np.sqrt(x[i]))
    out[ind] += np.pi
    ax.plot(thetaReal, out*180.0/np.pi, label='x={0}'.format(x[i]))
ax.set_xlabel(r'$\theta_m$')
ax.set_ylabel(r'$\theta_\mathrm{app}$')
pl.legend(loc='upper left')
pl.savefig('inclinationFilling.pdf')
pl.savefig('inclinationFilling.png')