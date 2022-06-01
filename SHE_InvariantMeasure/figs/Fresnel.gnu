# set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
# set output 'Fresnel.1.png'
set border 3 front lt black linewidth 1.000 dashtype solid
set key fixed left top vertical Left reverse enhanced autotitle nobox
set key invert samplen 4 spacing 1 width 0 height 0
set style data lines
set xtics border in scale 1,0.5 nomirror norotate  autojustify
set ytics border in scale 1,0.5 nomirror norotate  autojustify
set ytics  norangelimit 0.00000,0.25,0.750000
set cbtics border in scale 1,0.5 nomirror norotate  autojustify
set title "{/:Bold Fresnel integrals C(z), S(z)}" 
set title  offset character 0, -1, 0 font "" textcolor lt -1 norotate
set xrange [ 0.00000 : 3.14159 ] noreverse nowriteback
set x2range [ * : * ] noreverse writeback
set yrange [ 0.00000 : 1.00000 ] noreverse nowriteback
set y2range [ * : * ] noreverse writeback
set zrange [ * : * ] noreverse writeback
set cbrange [ * : * ] noreverse writeback
set rrange [ * : * ] noreverse writeback
set lmargin  10
set bmargin  4
set rmargin  10
set tmargin  4
NO_ANIMATION = 1
save_encoding = "utf8"
plot FresnelS(x), FresnelC(x), 0.5 lc "black" dt '...' notitle
