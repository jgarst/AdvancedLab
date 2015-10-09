all: latex

latex: 
	latexmk -silent Python-FirstSteps.tex
	latexmk -silent WritingSample.tex

	git diff ./Python-FirstSteps.pdf;\
	RETVAL=$$?; \
	if [ $$RETVAL -ne 0 ]; then \
	   cp ./Python-FirstSteps.pdf ./ClassMaterials; \
	fi

	git diff ./Python-FirstSteps.pdf;\
	RETVAL=$$?; \
	if [ $$RETVAL -ne 0 ]; then \
	  cp WritingSample.pdf ClassMaterials; \
	fi

clean: 
	latexmk -C

