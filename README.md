# KeyboardNavigation
Keyboard movement and selection and deletion to beginning of word and custom delimeters. Navigate fast between contiguous boundaries via visual inspection. For SublimeText ST2 ST3.

You always move to the beginning of places instead of non-deterministic (*beginning of of contiguous boundaries demarcated by whitespace). In the following sample you move to the delineated places. After you are at the beginning you move around from the beginning.

    |sample |text |thisisthebeginning |, |233434343

Therefore you know via visual inspection how many keystrokes to go to where you want to go. (preplanning of keystrokes).

This can be seen as analagous to mode in vim of move word to word of "w" and "b" and "W" and "B". But this expands it to arrow keys and extends it to all functions such as delete and backspace as well.

## Package Installation
* Manual method: Download ZIP from github. Extract the files to [Sublime_Data_Dir](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)\Packages\KeyboardNavigation
* Automatic method: Install 'KeyboardNavigation' from [Package Control](http://packagecontrol.io).

## Key Bindings Explanation
Recommended Keybindings:
* <kbd>ctrl+left</kbd> move cursor to *beginning of next contiguous boundary demarcated by whitespace
* <kbd>ctrl+right</kbd> move cursor to *beginning of previous contiguous boundary demarcated by whitespace
* <kbd>alt+left</kbd> move cursor to *beginning of previous subword boundary delineated by symbols
* <kbd>alt+right</kbd> move cursor to *beginning of next subword boundary delineated by symbols
* <kbd>home</kbd> move cursor to beginning of line limit (goes all the way to the beginning whereas the native one goes to beginning of indentation)
* <kbd>end</kbd> move cursor to end of line limit
* <kbd>ctrl+shift+left</kbd> select to *beginning of next contiguous boundary demarcated by whitespace
* <kbd>ctrl+shift+right</kbd> select to *beginning of previous contiguous boundary demarcated by whitespace
* <kbd>alt+shift+left</kbd> select to *beginning of previous subword boundary delineated by symbols
* <kbd>alt+shift+right</kbd> select to *beginning of next subword boundary delineated by symbols
* <kbd>shift+home</kbd> select to beginning of line (goes all the way to the beginning whereas the native one goes to beginning of indentation)
* <kbd>shift+end</kbd> select to end of line
* <kbd>ctrl+shift+w</kbd> expand selection to whitespace
* <kbd>ctrl+shift+e</kbd> expand selection to symbols
* <kbd>ctrl+shift+q</kbd> expand selection to quotes ", '
* <kbd>ctrl+shift+b</kbd> expand selection to brackets (, ), <, >, [, ], {, }
* <kbd>ctrl+shift+l</kbd> select line with linebreak
* <kbd>ctrl+alt+shift+l</kbd> select line without linebreak and prepending tab
* <kbd>ctrl+backspace</kbd> delete(backspace) to *beginning of previous contiguous boundary demarcated by whitespace
* <kbd>ctrl+delete</kbd> delete to next contiguous boundary demarcated by whitespace
* <kbd>alt+backspace</kbd> delete(backspace) to previous subword boundary delineated by symbols
* <kbd>alt+delete</kbd> delete to next subword boundary delineated by symbols
* <kbd>ctrl+o</kbd> delete line with linebreak
* <kbd>ctrl+alt+o</kbd> delete line without linebreak
* <kbd>ctrl+shift+c</kbd> copy full lines
* <kbd>ctrl+shift+x</kbd> cut full lines
* <kbd>ctrl+v</kbd> paste (differs from innate in that does not put a newline above when copy used from nonselection line)
* <kbd>ctrl+alt+v</kbd> paste on the line above (with a newline if not already one on the clipboard)
* <kbd>ctrl+alt+down</kbd> swap line down with up (native)
* <kbd>ctrl+alt+up</kbd> swap line up with down (native)
* <kbd>ctrl+d</kbd> duplicate line above (instead of below like innate one)
* <kbd>ctrl+alt+left</kbd> blank line above
* <kbd>ctrl+alt+right</kbd> blank line below
* <kbd>ctrl+alt+-</kbd> indent less (to the left)
* <kbd>ctrl+alt+=</kbd> indent more (to the right) (even works with blank line which the native one does not)

## Key Bindings Configuration
Since these are redefining / replacing your very basic navigational keys, the package does not automatically overwrite your existing key bindings. You must choose to add the keybindings yourself specific to your OS.

For Windows, you can use the recommended keybindings by adding the following lines to [Sublime_Data_Dir](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)\Packages\User\Default (Windows).sublime-keymap
```
{ "keys": ["ctrl+left"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+right"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": true} },
{ "keys": ["alt+left"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": false} },
{ "keys": ["alt+right"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["home"], "command": "kn_linelimit", "args": {"forward": false} },
{ "keys": ["end"], "command": "kn_linelimit", "args": {"forward": true} },

{ "keys": ["ctrl+shift+left"], "command": "select_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+shift+right"], "command": "select_to_beg_of_contig_boundary", "args": {"forward": true} },
{ "keys": ["alt+shift+left"], "command": "select_to_beg_of_subword_boundary", "args": {"forward": false} },
{ "keys": ["alt+shift+right"], "command": "select_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["shift+home"], "command": "select_to_kn_linelimit", "args": {"forward": false} },
{ "keys": ["shift+end"], "command": "select_to_kn_linelimit", "args": {"forward": true} },

{ "keys": ["ctrl+shift+w"], "command": "expand_selection_to_whitespace" },
{ "keys": ["ctrl+shift+e"], "command": "expand_selection_to_delims" },
{ "keys": ["ctrl+shift+q"], "command": "expand_selection_to_quotes"},
{ "keys": ["ctrl+shift+b"], "command": "expand_selection_to_brackets"},
{ "keys": ["ctrl+shift+l"], "command": "select_line" },
{ "keys": ["ctrl+alt+shift+l"], "command": "select_line_wo_linebreak" },

{ "keys": ["ctrl+backspace"], "command": "delete_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+delete"], "command": "delete_to_beg_of_contig_boundary", "args": {"forward": true} },
{ "keys": ["alt+backspace"], "command": "delete_to_beg_of_subword_boundary", "args": {"forward": false} },
{ "keys": ["alt+delete"], "command": "delete_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["ctrl+o"], "command": "delete_line" },
{ "keys": ["ctrl+alt+o"], "command": "delete_line_wo_linebreak" },

{ "keys": ["ctrl+shift+c"], "command": "copy_fulllines" },
{ "keys": ["ctrl+shift+x"], "command": "cut_fulllines" },
{ "keys": ["ctrl+v"], "command": "kn_paste" },
{ "keys": ["ctrl+alt+v"], "command": "paste_above_lines" },

{ "keys": ["ctrl+alt+up"], "command": "swap_line_up" },
{ "keys": ["ctrl+alt+down"], "command": "swap_line_down" },
{ "keys": ["ctrl+d"], "command": "kn_duplicate_line" },
{ "keys": ["ctrl+alt+left"], "command": "blankline_add", "args": {"forward": false} },
{ "keys": ["ctrl+alt+right"], "command": "blankline_add", "args": {"forward": true} },

{ "keys": ["ctrl+alt+-"], "command": "kn_indent", "args": {"forward": false} },
{ "keys": ["ctrl+alt+="], "command": "kn_indent", "args": {"forward": true} }
```
## How this compares with vim
Vim has this concept in a cryptic structure of "w" and "b" keys.

For a paradigm of where this is implemented in vim see "w" and "b" movement in vim. Each time the beginning of a word is moved to. There is also capital "W" and "B" for subwords. KeyboardNavigation brings this to you in the form of arrow keys.

[https://docs.oracle.com/cd/E19683-01/806-7612/6jgfmsvqf/index.html](https://docs.oracle.com/cd/E19683-01/806-7612/6jgfmsvqf/index.html) - Scroll to section "Moving One Word".  
[https://stackoverflow.com/questions/22931032/vim-word-vs-word](https://stackoverflow.com/questions/22931032/vim-word-vs-word) See definition of word vs WORD  
[https://www.computerhope.com/unix/vim.htm](https://www.computerhope.com/unix/vim.htm) - Scroll to section "Moving From Word To Word"  
[https://vim.rtorr.com/](https://vim.rtorr.com/) - See definition of "w" , "W" , "b" , "B"  
[https://forum.sublimetext.com/t/change-cursor-position-at-beginning-of-next-word-when-moving/21474](https://forum.sublimetext.com/t/change-cursor-position-at-beginning-of-next-word-when-moving/21474) - This concept is described here

Using the arrow keys is much more thought out. And using it with Ctrl and Alt is a way to make it accessible to the hand in a way which is spatially oriented. We know that we want to move to the word next and we want to move to the beginning so we know where we will go. Vim allows you to do this but with keys that are spaced far apart and not spatially oriented. Sublime has a way with KeyboardNavigation.

KeyboardNavigation allows contiguous boundary movement like vim's concept of "w" and "b" fastly through arrow keys that make sense and are thought out.
