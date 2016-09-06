:set tabstop=4 shiftwidth=4 expandtab

:function! s:guess_tab() abort
:   let lines = getline(1, 1024)
:   let tab_count = 0
:   let nonwhite_count = 0
:   for line in lines
:       if line =~# '.*\t'
:           let tab_count += 1
:       endif
:       if line =~# '.*\S'
:           let nonwhite_count += 1
:       endif
:   endfor
:   if tab_count > (nonwhite_count / 2)
:       call setbufvar('', '&'.'tabstop', 8)
:       call setbufvar('', '&'.'shiftwidth', 8)
:       call setbufvar('', '&'.'expandtab', 0)
:   endif
:endfunction

:autocmd BufRead * call s:guess_tab()


