mkfile_path := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

python_intro:
	(cd ${mkfile_path}; latexmk -silent Python-FirstSteps.tex \
		             && latexmk -c Python-FirstSteps.tex)

clean_python_intro:
	(cd ${mkfile_path}; latexmk -C $(mkfile_path)/Python-FirstSteps.tex)
