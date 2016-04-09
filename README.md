# KeyboardSelectionSublime
Keyboard movement and selection to custom delimeters. For SublimeText.

## Package Installation
* Manual method: Download ZIP from github. Extract the files to [Sublime_Data_Dir](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)\Packages\keyboardSelection
* Automatic method: Install 'keyboardSelectionSublime' from [Package Control](http://packagecontrol.io).

## Key Bindings
Sample keybindings:
* <kbd>ctrl+left</kbd> move to beginning of next contiguous boundary demarcated by a whitespace
* <kbd>ctrl+right</kbd> move to beginning of previous contiguous boundary demarcated by a whitespace
* <kbd>alt+left</kbd> move to beginning of previous subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>alt+right</kbd> move to beginning of next subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>ctrl+space</kbd> expand_selection_to_delims - expand selection to (space), \, ', -, (, ), <, >, [, ], {, }, :, ., (comma), %, @, &, (tab), (newline)
* <kbd>ctrl+shift+q</kbd> expand_selection_to_quotes - expand selection to ", '
* <kbd>ctrl+shift+b</kbd> expand_selection_to_brackets - expand selection to (, ), <, >, [, ], {, }
* <kbd>ctrl+delete</kbd> delete_to_beg_next_contig_boundary (delete to beginning of next contiguous boundary)

Since these are redefining your very basic navigational keys, the package does not automatically overwrite your existing key bindings. You must choose to add the keybindings yourself specific to your OS.

For Windows, you can use the recommended sample keybindings by adding the following lines to [Sublime_Data_Dir]\User\Default (Windows).sublime-keymap or [Sublime_Data_Dir]\KeyboardSelection\Default (Windows).sublime-keymap
```
{ "keys": ["ctrl+left"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+right"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": true} },

{ "keys": ["alt+left"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": false} },
{ "keys": ["alt+right"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["ctrl+space"], "command": "expand_selection_to_delims" },
{ "keys": ["ctrl+shift+q"], "command": "expand_selection_to_quotes"},
{ "keys": ["ctrl+shift+b"], "command": "expand_selection", "args": {"to": "brackets"} },
{ "keys": ["ctrl+delete"], "command": "delete_to_beg_next_contig_boundary" },
```
