# KeyboardNavigation
Keyboard movement and selection and deletion to whitespace and custom delimeters. Navigate fast between contiguous boundaries. For SublimeText ST2 ST3.

This is like mode in vim of move word to word of "w" and "b" and "W" and "B".

## Package Installation
* Manual method: Download ZIP from github. Extract the files to [Sublime_Data_Dir](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)\Packages\KeyboardNavigation
* Automatic method: Install 'KeyboardNavigation' from [Package Control](http://packagecontrol.io).

## Key Bindings Explanation
Sample Keybindings:
* <kbd>ctrl+left</kbd> move cursor to beginning of next contiguous boundary demarcated by a whitespace
* <kbd>ctrl+right</kbd> move cursor to beginning of previous contiguous boundary demarcated by a whitespace
* <kbd>alt+left</kbd> move cursor to beginning of previous subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>alt+right</kbd> move cursor to beginning of next subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>home</kbd> move cursor to beginning of line limit (goes all the way to the beginning whereas the native one goes to beginning of indentation)
* <kbd>end</kbd> move cursor to end of line limit
* <kbd>ctrl+shift+left</kbd> select to beginning of next contiguous boundary demarcated by a whitespace
* <kbd>ctrl+shift+right</kbd> select to beginning of previous contiguous boundary demarcated by a whitespace
* <kbd>alt+shift+left</kbd> select to beginning of previous subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>alt+shift+right</kbd> select to beginning of next subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>shift+home</kbd> select to beginning of line limit (goes all the way to the beginning whereas the native one goes to beginning of indentation)
* <kbd>shift+end</kbd> select to end of line limit
* <kbd>ctrl+shift+w</kbd> expand_selection_to_whitespace - expand selection to whitespace
* <kbd>ctrl+shift+e</kbd> expand_selection_to_delims - expand selection to (space), (tab), (newline), ", ', %, @, &, :, (period), (comma), +, _, -, <, >, (, ), [, ], {, }, |, \
* <kbd>ctrl+shift+q</kbd> expand_selection_to_quotes - expand selection to ", '
* <kbd>ctrl+shift+b</kbd> expand_selection_to_brackets - expand selection to (, ), <, >, [, ], {, }
* <kbd>ctrl+shift+l</kbd> select line with linebreak
* <kbd>ctrl+alt+shift+l</kbd> select line without linebreak
* <kbd>ctrl+backspace</kbd> delete(backspace) to previous contiguous boundary demarcated by a whitespace
* <kbd>ctrl+delete</kbd> delete to next contiguous boundary demarcated by a whitespace
* <kbd>alt+backspace</kbd> delete(backspace) to previous subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>alt+delete</kbd> delete to next subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>ctrl+o</kbd> delete line with linebreak
* <kbd>ctrl+alt+o</kbd> delete line without linebreak
* <kbd>ctrl+shift+c</kbd> copy full lines
* <kbd>ctrl+shift+x</kbd> cut full lines
* <kbd>ctrl+v</kbd> paste (differs from innate in that does not put a newline above when copy used from nonselection line)
* <kbd>ctrl+alt+v</kbd> paste with newline above
* <kbd>ctrl+alt+down</kbd> swap line down with up (native)
* <kbd>ctrl+alt+up</kbd> swap line up with down (native)
* <kbd>ctrl+d</kbd> duplicate line above (instead of below like innate one)
* <kbd>ctrl+alt+left</kbd> blank line above and be there
* <kbd>ctrl+alt+right</kbd> blank line below and be there
* <kbd>ctrl+alt+-</kbd> indent less (to the left)
* <kbd>ctrl+alt+=</kbd> indent more (to the right) (even works with blank line which the native one does not)

## Key Bindings Configuration
Since these are redefining / replacing your very basic navigational keys, the package does not automatically overwrite your existing key bindings. You must choose to add the keybindings yourself specific to your OS.

For Windows, you can use the recommended sample keybindings by adding the following lines to [Sublime_Data_Dir](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)\Packages\User\Default (Windows).sublime-keymap
```
{ "keys": ["ctrl+left"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+right"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": true} },
{ "keys": ["alt+left"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": false} },
{ "keys": ["alt+right"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["home"], "command": "kn_linelimit", "args": {"forward": false} },
{ "keys": ["end"], "command": "kn_linelimit", "args": {"forward": true} },

{ "keys": ["ctrl+shift+left"], "command": "select_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+shift+right"], "command": "select_to_beg_of_contig_boundary", "args": {"forward": true} },
{ "keys": ["alt+shift+left"], "command": select_to_beg_of_subword_boundary "args": {"forward": false} },
{ "keys": ["alt+shift+right"], "command": "select_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["shift+home"], "command": "select_to_kn_linelimit", "args": {"forward": false} },
{ "keys": ["shift+end"], "command": "select_to_kn_linelimit", "args": {"forward": true} },

{ "keys": ["ctrl+shift+w"], "command": "expand_selection_to_whitespace" },
{ "keys": ["ctrl+shift+e"], "command": "expand_selection_to_delims" },
{ "keys": ["ctrl+shift+q"], "command": "expand_selection_to_quotes"},
{ "keys": ["ctrl+shift+b"], "command": "expand_selection_to_brackets"},
{ "keys": ["ctrl+shift+l"], "command": "select_line" },
{ "keys": ["ctrl+alt+shift+l"], "command": select_line_wo_linebreak },

{ "keys": ["ctrl+backspace"], "command": "delete_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+delete"], "command": "delete_to_beg_of_contig_boundary", "args": {"forward": true} },
{ "keys": ["alt+backspace"], "command": "delete_to_beg_of_subword_boundary", "args": {"forward": false} },
{ "keys": ["alt+delete"], "command": "delete_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["ctrl+o"], "command": "delete_line" },
{ "keys": ["ctrl+alt+o"], "command": "delete_line_wo_linebreak" },

{ "keys": ["ctrl+shift+c"], "command": "copy_fulllines" },
{ "keys": ["ctrl+shift+x"], "command": "cut_fulllines" },
{ "keys": ["ctrl+v"], "command": "kn_paste" },
{ "keys": ["ctrl+alt+v"], "command": "paste_into_lines" },

{ "keys": ["ctrl+alt+up"], "command": "swap_line_up" },
{ "keys": ["ctrl+alt+down"], "command": "swap_line_down" },
{ "keys": ["ctrl+d"], "command": "kn_duplicate_line" },
{ "keys": ["ctrl+alt+left"], "command": "blankline_add", "args": {"forward": false} },
{ "keys": ["ctrl+alt+right"], "command": "blankline_add", "args": {"forward": true} },

{ "keys": ["ctrl+alt+-"], "command": "kn_indent", "args": {"forward": false} },
{ "keys": ["ctrl+alt+="], "command": "kn_indent", "args": {"forward": true} }
```
## How this compares with vim
For a paradigm of where this is implemented in vim -  
[https://docs.oracle.com/cd/E19683-01/806-7612/6jgfmsvqf/index.html](https://docs.oracle.com/cd/E19683-01/806-7612/6jgfmsvqf/index.html)  
[https://stackoverflow.com/questions/22931032/vim-word-vs-word](https://stackoverflow.com/questions/22931032/vim-word-vs-word)  
[https://www.computerhope.com/unix/vim.htm](https://www.computerhope.com/unix/vim.htm) - "Moving From Word To Word"  
[https://vim.rtorr.com/](https://vim.rtorr.com/)  
[https://forum.sublimetext.com/t/change-cursor-position-at-beginning-of-next-word-when-moving/21474](https://forum.sublimetext.com/t/change-cursor-position-at-beginning-of-next-word-when-moving/21474)
```
Press w (“WORD”) to move the cursor to the right one word at a time.
Press b (“BACK”) to move the cursor to the left one word at a time.
Press W (“word”) to move the cursor to the right one word at a time. (words can contain punctuation)
Press B (“back”) to move the cursor to the left one word at a time. (words can contain punctuation)
```

KeyboardNavigation allows vim "w" and "b" like movement fastly through contiguous boundaries.
