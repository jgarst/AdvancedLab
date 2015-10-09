all: FWHM

FWHM.ipynb: FWHM

FWHM:
	python3 ../../generate_document.py FWHM.order
	ipython nbconvert --execute FWHM.ipynb --to notebook --output FWHM.ipynb
