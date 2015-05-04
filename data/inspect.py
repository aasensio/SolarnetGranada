import numpy as np
import matplotlib.pyplot as pl

class inspector(object):

	def __init__(self):
		"""
		Init
				
		"""
		pl.close('all')
		self.mapsFig, self.axMaps = pl.subplots(nrows=2, ncols=2, figsize=(12,12))
		self.stokesFig, self.axStokes = pl.subplots(nrows=4, ncols=1, figsize=(12,12))
		self.xdata = 0
		self.ydata = 0

	def onMove(self, event):
		"""
		Function that is called whenever the mouse moves
		
		Args:
		    event : event triggered
		
		"""
		if (event.xdata != None and event.ydata != None and event.xdata != self.xdata and event.ydata != self.ydata):

			self.xdata = event.xdata
			self.ydata = event.ydata

			for loop in range(4):
				self.stokesFig.canvas.restore_region(self.background[loop])
				self.obsStokes[loop].set_ydata(self.stokes[loop][event.ydata, event.xdata, :])
				self.axStokes[loop].draw_artist(self.obsStokes[loop])
				self.axStokes[loop].draw_artist(self.axStokes[loop].get_yaxis())
				self.stokesFig.canvas.blit(self.axStokes[loop].bbox.expanded(1.4, 1.1))
	

	def onClick(self, event):
		"""
		Function that is called whenever the mouse is clicked
		
		Args:
		    event: event triggered

		"""
		if (event.button == 1):
			for loop in range(1,4):
				self.limits[loop,:] *= 0.5

		if (event.button == 3):
			for loop in range(1,4):
				self.limits[loop,:] *= 2.0

		if (event.button == 2):
			self.mapsFig.canvas.mpl_disconnect(self.motionEvent)
			self.mapsFig.canvas.mpl_disconnect(self.clickEvent)
			pl.close('all')

		for loop in range(4):			
			self.axStokes[loop].set_ylim(self.limits[loop,:])

	def loadDataNPY(self, stIFile, stQFile, stUFile, stVFile, ranges=None):
		"""
		Load the data from npy files
		
		Args:
		    stIFile (string): file with Stokes I
		    stQFile (string): file with Stokes Q
		    stUFile (string): file with Stokes U
		    stVFile (string): file with Stokes V
		    ranges (int, optional): wavelength range where to compute the images
		
		"""
		self.stokes = [None] * 4
		self.stokes[0] = np.load(stIFile)
		self.stokes[1] = np.load(stQFile)
		self.stokes[2] = np.load(stUFile)
		self.stokes[3] = np.load(stVFile)

		if (ranges == None):
			ranges = [0, len(self.stokes[0][0,0,:])]

		self.stIMap = np.sum(self.stokes[0][:,:,ranges[0]:ranges[1]], axis=2)
		self.stQMap = np.sum(self.stokes[1][:,:,ranges[0]:ranges[1]], axis=2)
		self.stUMap = np.sum(self.stokes[2][:,:,ranges[0]:ranges[1]], axis=2)
		self.stVMap = np.sum(self.stokes[3][:,:,ranges[0]:ranges[1]], axis=2)

		self.limits = np.zeros((4,2))
		for loop in range(4):
			self.limits[loop,:] = [np.min(self.stokes[loop]), np.max(self.stokes[loop])]

	def inspect(self):
		"""
		Inspect the data
				
		"""
		self.axMaps[0,0].imshow(self.stIMap, cmap=pl.cm.gray)
		self.axMaps[0,1].imshow(self.stQMap, cmap=pl.cm.gray)
		self.axMaps[1,0].imshow(self.stUMap, cmap=pl.cm.gray)
		self.axMaps[1,1].imshow(self.stVMap, cmap=pl.cm.gray)

		self.mapsFig.show()

		self.obsStokes = [None] * 4

		self.obsStokes[0], = self.axStokes[0].plot(self.stokes[0][self.xdata, self.ydata, :], animated=True)
		self.obsStokes[1], = self.axStokes[1].plot(self.stokes[1][self.xdata, self.ydata, :], animated=True)
		self.obsStokes[2], = self.axStokes[2].plot(self.stokes[2][self.xdata, self.ydata, :], animated=True)
		self.obsStokes[3], = self.axStokes[3].plot(self.stokes[3][self.xdata, self.ydata, :], animated=True)

		for loop in range(4):			
			self.axStokes[loop].set_ylim(self.limits[loop,:])

		self.stokesFig.show()

		self.background = [None] * 4
		for i in range(4):
			self.background[i] = self.stokesFig.canvas.copy_from_bbox(self.axStokes[i].bbox.expanded(1.4, 1.1))

		self.motionEvent = self.mapsFig.canvas.mpl_connect('motion_notify_event', self.onMove)
		self.clickEvent = self.mapsFig.canvas.mpl_connect('button_press_event', self.onClick)


which = 'sunspot'
out = inspector()
if (which == 'sunspot'):
	out.loadDataNPY('stokesI_sunspot.npy', 'stokesQ_sunspot.npy', 'stokesU_sunspot.npy', 'stokesV_sunspot.npy')
if (which == 'prominence'):
	out.loadDataNPY('stokesI_prominence.npy', 'stokesQ_prominence.npy', 'stokesU_prominence.npy', 'stokesV_prominence.npy', ranges=[400,600])
out.inspect()
