import pyfits as pf
import numpy as np

# Transform the files in numpy format to fits
for region in ['sunspot', 'prominence']:
	for l in ['I', 'Q', 'U', 'V']:
		stI = np.load('stokes{0}_{1}.npy'.format(l,region))
		hdu = pf.PrimaryHDU(stI)
		hdu.writeto('stokes{0}_{1}.fits'.format(l,region))
