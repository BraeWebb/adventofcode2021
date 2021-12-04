#ensure_path( 'TEXINPUTS', '../../tex//' );
#ensure_path( 'BIBINPUTS', '../../references//' );

#$bibtex = "bibtex -include-directory=../../references %O %B";

@default_files = ('aoc.tex');

$pdflatex = 'pdflatex -interaction=nonstopmode -shell-escape';
$out_dir = 'out';

$pdf_mode = 1;