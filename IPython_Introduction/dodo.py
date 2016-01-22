from os import path, listdir
from doit.task import clean_targets


DOIT_CONFIG = {'default_tasks': ['python_firststeps']}

NOTEBOOKS = [path.splitext(notebook)[0]
             for notebook in listdir('notebooks')
             if notebook[-6:] == '.ipynb']


def task_python_firststeps():
    """Creates python firststeps pdf"""
    return {
            'actions': [['latexmk', '-silent', 'Python-FirstSteps.tex'],
                        ['latexmk', '-c', 'Python-FirstSteps.tex']],
            'targets': ['Python-FirstSteps.pdf'],
            'file_dep': ['{0}.tex'.format(notebook)
                         for notebook in NOTEBOOKS] +
                         ['Python-FirstSteps.tex',
                          'tufte-handout-local.tex'],
            'clean': [clean_targets,
                      'rm -rf _minted-Python-FirstSteps']
            }


def task_convert_notebook():
    """Converts ipython notebook to inlineable .tex"""

    for notebook in NOTEBOOKS:
        datafile = 'notebooks/{0}.csv'.format(notebook)

        dependencies = ['notebooks/{0}.ipynb'.format(notebook),
                        'notebooks/hide_warnings.tplx']

        if path.isfile(datafile):
            dependencies += [datafile]

        yield {
            'name': notebook,
            'actions': [['jupyter', 'nbconvert',
                         '--to', 'latex',
                         # '--ExecutePreprocessor.enabled=True',
                         '--template', 'notebooks/hide_warnings.tplx',
                         'notebooks/{0}.ipynb'.format(notebook)]],

            'targets': ['{0}.tex'.format(notebook)],

            'file_dep': dependencies,

            'clean': [clean_targets,
                      'rm -rf {0}_files'.format(notebook)]

        }
