Problem:
  Best practices for displaying problems and solutions depends
  on the format. Printable documents should be in latex,
  solutions should be in IPython notebooks, interactive excersizes
  should be in html. Nominally IPython notebooks provide all these
  functions, but practically keeping everything in markdown
  prohibits advanced typesetting and portability.

Solution:
  Components of the problem will be kept in many .tex code
  files that will specify a 'format' for the document, each cell with a
  'filename' and optionally a 'type' in a json problem.order file. These
  templates will be assembled with nb_generate.py.

Advantage:
  This will allow each component of a problem to be written
  once instead of once in each of the possible combinations of format,
  target student, document intent. For example, a hint can be
  displayed in the margin of a printed document, or in a rich way
  within an html file.
