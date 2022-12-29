# Use this script to extract all tikz figures from a tex file:

1. All environments with the name "tikzpicture" are extracted.
2. Each figure is saved in a separate file.
3. Figure files will be named "figure_1.tex", "figure_2.tex", etc.
4. The original tex file is not modified.
5. The figure tex files are processed to generate pdf figure files without margin.
6. Edit [extractFigure tex](./extractFigure.tex) for preamble and other options.
  1. For example, if one want to use the cross reference, one needs to give the main file name without extension. Make sure the mainfile has been compiled and the .aux file exists.

## Acknowledgements: 
1. Chatgpt
2. Github Copilot

