all: FirstMoments

FirstMoments.ipynb: FirstMoments

FirstMoments:
	python3 ../../generate_document.py FirstMoments.order
	ipython nbconvert --execute FirstMoments.ipynb --to notebook --output FirstMoments.ipynb
