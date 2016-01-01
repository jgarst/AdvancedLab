mkfile_path := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

python_intro:
	(cd ${mkfile_path}; latexmk -silent -bibtex- Python-FirstSteps.tex)
	(cd ${mkfile_path}; latexmk -c $(mkfile_path)/Python-FirstSteps.tex)

clean_python_intro:
	(cd ${mkfile_path}; latexmk -C $(mkfile_path)/Python-FirstSteps.tex)
