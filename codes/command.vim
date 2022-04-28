" noremap <leader><leader> :w <bar>:!./SamplePathAni.py 3 & <cr>
noremap <leader><leader> :w <bar>:!.% & <cr>
" function! CopyAllBib()
"   " echom "Run biber now..."
"   let filenameRoot=expand("%:r")
"   let execstr="AsyncRun! rsync ~/Dropbox/workspace/svn/refdb/All.bib All.bib "
"   exec execstr
"   let g:asyncrun_exit = 'silent :lua require("notify")("Synchronized All.bib~! -- Le", "info")'
" endfunction
" autocmd FileType tex noremap <leader><leader> :update<bar>:call CopyAllBib()<CR>
