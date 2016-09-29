:highlight ExtraWhitespace ctermbg=red guibg=red
" Show trailing whitespace:
:autocmd BufWinEnter * match ExtraWhitespace /\s\+$/

:set tabstop=4 shiftwidth=4 expandtab

:highlight WrongIndent ctermbg=red guibg=red

" Count number of lines that begin with at least 1 tab,
" and lines that start with at least one whitespace character in general.
:function! s:guess_tab() abort
:   let lines = getline(1, 1024)
:   let tab_count = 0
:   let white_count = 0
:   for line in lines
:       if line =~# '^\t\+'
:           let tab_count += 1
:       endif
"       Don't count lines with only whitespace
:       if line =~# '^\s\+\S'
:           let white_count += 1
:       endif
:   endfor
:   if tab_count > (white_count / 2)
:       call setbufvar('', '&'.'tabstop', 8)
:       call setbufvar('', '&'.'shiftwidth', 8)
:       call setbufvar('', '&'.'expandtab', 0)
:       autocmd BufWinEnter * match WrongIndent /^ \+/
:   else
:       autocmd BufWinEnter * match WrongIndent /^\t\+/
:   endif
:endfunction

:autocmd BufRead * call s:guess_tab()
