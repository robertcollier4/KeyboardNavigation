# KeyboardNavigation
Keyboard movement and selection and deletion to custom delimeters. Navigate fast between contiguous boundaries. For SublimeText.

## Package Installation
* Manual method: Download ZIP from github. Extract the files to [Sublime_Data_Dir](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)\Packages\KeyboardNavigation
* Automatic method: Install 'KeyboardNavigation' from [Package Control](http://packagecontrol.io).

## Key Bindings
Sample keybindings:
* <kbd>ctrl+left</kbd> move to beginning of next contiguous boundary demarcated by a whitespace
* <kbd>ctrl+right</kbd> move to beginning of previous contiguous boundary demarcated by a whitespace
* <kbd>alt+left</kbd> move to beginning of previous subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>alt+right</kbd> move to beginning of next subword boundary delineated by ", ., +, _, <, >, [, ], {, }, -, (, )
* <kbd>home</kbd> move to beginning of line (including if it has indentation)
* <kbd>end</kbd> move to end of line
* <kbd>ctrl+alt+-</kbd> indent less
* <kbd>ctrl+alt+=</kbd> indent more (even works with blank line)
* <kbd>ctrl+shift+w</kbd> expand_selection_to_whitespace - expand selection to whitespace
* <kbd>ctrl+shift+e</kbd> expand_selection_to_delims - expand selection to (space), (tab), (newline), ", ', %, @, &, :, (period), (comma), +, _, -, <, >, (, ), [, ], {, }, |, \
* <kbd>ctrl+shift+q</kbd> expand_selection_to_quotes - expand selection to ", '
* <kbd>ctrl+shift+b</kbd> expand_selection_to_brackets - expand selection to (, ), <, >, [, ], {, }
* <kbd>ctrl+shift+l</kbd> expand selection to line (native)
* <kbd>ctrl+backspace</kbd> delete to previous contiguous boundary demarcated by a whitespace
* <kbd>ctrl+delete</kbd> delete to next contiguous boundary demarcated by a whitespace

Since these are redefining your very basic navigational keys, the package does not automatically overwrite your existing key bindings. You must choose to add the keybindings yourself specific to your OS.

For Windows, you can use the recommended sample keybindings by adding the following lines to [Sublime_Data_Dir]\User\Default (Windows).sublime-keymap
```
{ "keys": ["ctrl+left"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+right"], "command": "move_to_beg_of_contig_boundary", "args": {"forward": true} },

{ "keys": ["alt+left"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": false} },
{ "keys": ["alt+right"], "command": "move_to_beg_of_subword_boundary", "args": {"forward": true} },

{ "keys": ["home"], "command": "homeendbeginning", "args": {"forward": false} },
{ "keys": ["end"], "command": "homeendbeginning", "args": {"forward": true} },

{ "keys": ["ctrl+alt+-"], "command": "indentblankline", "args": {"forward": false} },
{ "keys": ["ctrl+alt+="], "command": "indentblankline", "args": {"forward": true} }

{ "keys": ["ctrl+shift+w"], "command": "expand_selection_to_whitespace" },
{ "keys": ["ctrl+shift+e"], "command": "expand_selection_to_delims" },
{ "keys": ["ctrl+shift+q"], "command": "expand_selection_to_quotes"},
{ "keys": ["ctrl+shift+b"], "command": "expand_selection_to_brackets"},
{ "keys": ["ctrl+shift+l"], "command": "expand_selection", "args": {"to": "line"} },

{ "keys": ["ctrl+backspace"], "command": "delete_to_beg_of_contig_boundary", "args": {"forward": false} },
{ "keys": ["ctrl+delete"], "command": "delete_to_beg_of_contig_boundary", "args": {"forward": true} },
```
