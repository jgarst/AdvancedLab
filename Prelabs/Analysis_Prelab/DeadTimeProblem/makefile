TEMPLATE = DeadTime.order
NOTEBOOK = DeadTime.ipynb

all: DeadTime

DeadTime.ipynb: DeadTime

DeadTime:
	python3 ../../generate_document.py $(TEMPLATE)
	ipython nbconvert --execute $(NOTEBOOK) --to notebook --output $(NOTEBOOK)
