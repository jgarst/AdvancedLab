import IPython.nbformat as nbf
import json
import argparse
import os.path
import pypandoc
from IPython.nbconvert.preprocessors import execute

class ConvertPython:
    format = 'python'
    
    def toIPythonCell(cellText):
        return nbf.v4.new_code_cell(cellText)

class ConvertLatex:
    format = 'latex'
    
    def toIPythonCell(cellText):
        cellText = pypandoc.convert(cellText, 
                                    to=ConvertMarkdown.format, 
                                    format=ConvertLatex.format)
        return nbf.v4.new_markdown_cell(cellText)
    
class ConvertMarkdown:
    # markdown simple tables do not align properly
    # do not use them.
    format = 'markdown-simple_tables'
    
    def toIPythonCell(cellText):
        return nbf.v4.new_markdown_cell(cellText) 

# assumption is that pandoc will react gracefully to unnecessary
# extensions in to and from commands
conversions = {'.ipynb':None,
              'markdown':ConvertMarkdown,
              'md':ConvertMarkdown,
              '.md':ConvertMarkdown,
              'python':ConvertPython, 
              'py':ConvertPython, 
              '.py':ConvertPython,
              'latex':ConvertLatex, 
              'tex':ConvertLatex, 
              '.tex':ConvertLatex}

def fileExists(fp):
    return os.path.isfile(fp) and os.stat(fp).st_size != 0

def readFile(fp):
    if fileExists(fp):
        with open(fp) as f: fileText = f.read()
    else:
        fileText = ''
    
    return fileText

# always overwrites notebook
def getNotebook(fp):
    return nbf.v4.new_notebook()

def writeQuestionNotebooks(fp, nb):
    with open(fp, 'w') as f:
        nbf.write(nb, f)

if __name__ == "__main__":    
    desc = "convert latex and code into ipython notebook"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("template", nargs='+',
                        help="the template to generate")
    
    args = parser.parse_args()    
    for fp in args.template:
        with open(fp, 'r') as f:
            template = json.load(f)

        templateDir = os.path.split(fp)[0]
        templateRoot = os.path.splitext(fp)[0]

        nb_fp = templateRoot + template['format']
        nb = getNotebook(nb_fp)
    
        #currently overwrites whatever is in notebook
        nb['cells'] = []
        for c in template['cells']:
            fp = os.path.join(templateDir, c['file'])
            cellText = readFile(fp)
            if 'fromFormat' not in c:
                c['fromFormat'] = os.path.splitext(fp)[1]
            convert = conversions[c['fromFormat']]
            cell = convert.toIPythonCell(cellText)
            nb['cells'].append(cell)
    
        writeQuestionNotebooks(fp = nb_fp, nb = nb)
        
    



