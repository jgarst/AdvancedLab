mkfile_path := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

python_intro: first_example.tex
	(cd ${mkfile_path}; latexmk -silent Python-FirstSteps.tex \
		             && latexmk -c Python-FirstSteps.tex)

clean_python_intro:
	(cd ${mkfile_path}; latexmk -C $(mkfile_path)/Python-FirstSteps.tex)
	-rm -f first_example.tex
	-rm -rf _minted-Python-FirstSteps
	-rm -rf first_example_files

first_example.tex: first_example.ipynb hide_warnings.tplx
	jupyter nbconvert --to latex \
					  --ExecutePreprocessor.enabled=True \
					  --template ./hide_warnings.tplx \
					  first_example.ipynb
