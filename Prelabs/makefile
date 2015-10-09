ANALYSIS_TEMPLATES = $(shell find Analysis_Prelab -type f -name '*.order')
NOTEBOOKS = $(subst .order,.ipynb,$(ANALYSIS_TEMPLATES))

all: analysis

analysis: $(ANALYSIS_TEMPLATES)
	$(foreach TEMPLATE,$(ANALYSIS_TEMPLATES), \
		$(eval NB=$(subst .order,.ipynb,$(TEMPLATE))) \
		python3 generate_document.py $(TEMPLATE); \
		ipython nbconvert --execute $(NB) --to notebook --output $(NB);)
