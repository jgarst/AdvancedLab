$pdf_mode = 1;
$pdflatex = "pdflatex --shell-escape -interaction=batchmode %O %S";
$pdf_previewer = 'evince';
#$aux_dir = 'aux';


@default_files = ("Python-FirstSteps.tex", "WritingSample.tex");

$out_dir = "ClassMaterials";

# Do not run a previewer
$preview_mode = 0;

# Do not watch for updated files
$preview_continuous_mode = 0;

