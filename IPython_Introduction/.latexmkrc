$pdf_mode = 1;
$pdflatex = "pdflatex --shell-escape -interaction=batchmode %O %S";
$pdf_previewer = 'evince';
#$aux_dir = 'aux';

# Remove all files except dvi, ps, pdf
$cleanup_mode = 2;

@default_files = ("Python-FirstSteps.tex", "WritingSample.tex");

$outdir = "ClassMaterials";

# Do not run a previewer
$preview_mode = 0;

# Do not watch for updated files
$preview_continuous_mode = 0;

