#!/usr/bin/env python3
# By Le Chen
# chenle02@gmail.com / le.chen@auburn.edu
#

import re
import subprocess

# Check arguments and set variables
import argparse
parser = argparse.ArgumentParser(description='Extract tikz figures from a LaTeX file')
parser.add_argument('-i', '--input', help='input LaTeX file', required=False)
parser.add_argument('-s', '--show', help='Show figure pdf files using zathura', required=False)
args = parser.parse_args()

# Parser an boolean argument given to show
if args.show:
    if args.show.lower() in ['true', 't', 'yes', 'y', '1']:
        show = True
    else:
        show = False

# Test if argument, args.input is given, if not given, give a default value; if
# given, test if the file is readable. In any case, use the variable
# MainTexFile to store the filename.
if args.input:
    MainTexFile = args.input
else:
    MainTexFile = 'Invariant_Measure_SHE.tex'

try:
    f = open(MainTexFile, 'r')
    f.close()
except IOError:
    print('File not found or not readable')


# Open the LaTeX file and read its contents into a string
with open('Invariant_Measure_SHE.tex', 'r') as f:
    contents = f.read()

# Find all the TikZ figures in the file using a regular expression
tikz_figures = re.findall(r'\\begin{tikzpicture}(.+?)\\end{tikzpicture}', contents, flags=re.DOTALL)

# Extract the caption and label for each figure
captions = []
labels = []
for figure in tikz_figures:
    caption_match = re.search(r'\\caption{(.+?)}', figure)
    label_match = re.search(r'\\label{(.+?)}', figure)
    if caption_match:
        captions.append(caption_match.group(1))
    else:
        captions.append('')
    if label_match:
        labels.append(label_match.group(1))
    else:
        labels.append('')

# Save each figure to a separate file
for i, figure in enumerate(tikz_figures):
    with open(f'figure_{i+1}.tikz', 'w') as f:
        f.write(figure)

# Create a standalone LaTeX file for each TikZ figure
for i, figure in enumerate(tikz_figures):
    with open(f'figure_{i+1}.tex', 'w') as f:
        f.write(f'\
\\documentclass[varwidth=\\maxdimen]{{standalone}}\n\
\\input{{CommonPreamble.tex}}\n\
\\begin{{document}}\n\
\\begin{{tikzpicture}}\n\
    {figure}\n\
\\end{{tikzpicture}}\n\
\\end{{document}}\
')

# Compile each TikZ file into an EPS file
for i, figure in enumerate(tikz_figures):
    subprocess.run(['pdflatex', f'figure_{i+1}.tex'])
    if show:
        subprocess.Popen(['zathura', f'figure_{i+1}.pdf'], start_new_session=True)
