# Lectures on Solar magnetic fields: diagnostics and applications
3rd SOLARNET School on "Solar Magnetic Fields: Modeling and Measuring Techniques", 18-23 May 2015, Granada, Spain

These repository contains the slides and codes that are part of the lecture.

## Slides
The slides are provided in Powerpoint format. The final version will be transformed to pdf.

## Codes
All programs are coded in Python. They need the following dependencies so you need to have them
installed in your system in case you want to use them:

* Numpy
* Scipy
* Matplotlib

Some routines make use of synthesis codes that I have in my repository. Check [this](https://github.com/aasensio/lte) and [this](https://github.com/aasensio/milne) repos.

## Data
We will be using some observations during the lectures. You can [download](https://www.dropbox.com/sh/ukawbdb7w75g5u0/AAA1I-xwr_-mVZ_5mE50a32Na?dl=0) them before
the lectures so that we can all play together with them. The data is in numpy binary format and also in fits format.

## IPython Notebooks
During the lectures, I will show some practical results using IPython Notebooks. Github currently renders them
by clicking on the link. However, here are the links to the them:

* [Asymmetries](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Asymmetries.ipynb)
* [Atomic parameters](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Atomic%20parameters.ipynb)
* [Empire Strikes Back Priors](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Empire%20Strikes%20Back%20Priors.ipynb)
* [Linear Fit](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Linear%20Fit.ipynb)
* [Principal Component Analysis](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/PCA.ipynb)
* [Python tools](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Python%20tools.ipynb)
* [Simple diagnostics](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Simple%20diagnostics.ipynb)
* [Stray-light](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Stray-light.ipynb)
* [Weak-field approximation](http://nbviewer.ipython.org/github/aasensio/SolarnetGranada/blob/master/notebooks/Weak%20field%20approximation.ipynb)

## Outline

### Lecture 1 - Introduction
* Stokes profiles in different structures
* Physical intuition from profiles
* Web+python useful tools
* Noise and denoising
* NLTE & Hanle effect
* Stray-light
* Atomic parameters
* Zeeman vs. Paschen-Back
* Azimuth disambiguation

### Lecture 2 - Simplified diagnostics
* Simplified diagnostics
* Weak-field approximation
* Strong-field approximation
* Longitudinal and vector magnetographs
* Bisector and center-of-gravity techniques
* Unresolved fields
* Asymmetries

### Lecture 3 - Model fitting
* The four rules
* Generative models
* Likelihood functions
* Priors
* Nuisance parameters
* Outliers

### Lecture 4 - Nonlinear inversions
* Maximum-likelihood simple solution
* Weak-field
* More complicated cases using response functions
* Levenberg-Marquardt
* Milne-Eddington solution
* Local thermodynamic equilibrium
* Non-local thermodynamic equilibrium
* Database search
* New methods

### Lecture 5 - Scattering polarization and the Hanle effect
* The classical view
* Regimes
* The quantum approach
* Atomic polarization
* The two-level atom
* Some observations
* Hazel
* Applications

### Practical session
Choose one exercise among the following list
* Create a simple inversion code using the Python machinery available
in my repository
* Use the simplified diagnostics for inferring some properties of the
maps provided in the repository.
