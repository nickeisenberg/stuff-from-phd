set tw=100
" noremap <leader><leader> :w<cr>:!lualatex ./Invariant_Measure_SHE_JPT.tex<cr>
noremap <leader>b :w<cr>:!bibtex ./Invariant_Measure_SHE_JPT<cr>
noremap <leader><cr> :vsp ./Invariant_Measure_SHE_JPT.tex <cr> :windo diffthis<cr>

