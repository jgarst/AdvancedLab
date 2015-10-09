all: IPython DataAnalysis prelabs

prelabs:
	$(MAKE) -C Prelabs

IPython:
	$(MAKE) -C IPython_Introduction

DataAnalysis:
	$(MAKE) -C Analysis_Prelab

clean:
	$(MAKE) -C IPython_Introduction clean

push: all
	git remote | xargs -L1 git push --all
	aws s3 sync ClassMaterials/ s3://cultofjared --exclude ".ipynb_checkpoints/*"
