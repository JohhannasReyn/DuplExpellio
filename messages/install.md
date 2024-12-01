
### ____________________________DuplExpellio_______________________________ ###

# ~~This plugin allows you to select or remove duplicate entries like magic.~~ #

## Usage ##

  - Navigate to: `Edit`->`Remove Duplicates` to remove all **duplicates** or, 
    Navigate to: `Selection`->`Expand Selection to Duplicates` to select them.

    **Duplicates** - meaning redundant entries either separated by a new line, a comma, ',', a semi-colon, ';', or separated by a space, ' ' (effectively selecting all redundant words). This ordering used in determining is defined
    in settings and can be modified to use any string as a delimiter you wish to use.
    
    **Delimiters** - the character or string of characters used to separate entries among
    a collection of entries.

    - Delimiters are chosen if there are enough of them to meet the minimum qualifying amount.
    
    - This minimum qualifying amount can be adjusted via settings as the value of 'threshold'.
        $~ The default value for `threshold` is 8 ~$, meaning if 8 or more delimiting characters
        or strings of characters are found, it qualifies and will be used as a delimiter; 
        otherwise, the program moves down the list until a qualifying delimiter is found in the 
        **targeted text**.

    - The list of delimiters can be modified to fit your specific need via the settings: `Preferences`->`Package Settings`->`DuplExpellio`->`Settings`

    **Targeted Text** - if you wish to target a specific section of text within a file, simply select the text to search within the selected portion only. If no text is selected, the entire file is checked for duplicates.

## Key Bindings ##

**To Implement** the suggested key bindings goto the menu, and select:

`Preferences`->`Key Bindings` 

and in the right pane, append the following to the end of the json:

```json

    ,  // <-- The last entry before the closing curly bracket will need a comma after it.

    // Select duplicates using qualifying delimiter
    { "keys": ["alt+shift+d"], "command": "select_duplicates"},

    // Remove duplicates using qualifying delimiter
    { "keys": ["alt+shift+x"], "command": "remove_duplicates"}

} // <-- closing curly bracket (is already there)
```
    
add the entries above before the last closing bracket '}'
    
**The entry just before these two entries will be needing a comma after it.**

You can search the keybindings in the left pane using `ctrl+F` to ensure there are no conflicting key mappings with this plugins suggested key mapping.

## Settings ##

**delimiters**: this is a list of delimiters the plugin will attempt to use to separate the entries, in the order they are checked to see if they qualify as a delimiter. ['\n',',',';',' '] (i.e. new line, comma, semi-colon, space)
    *Note*: the last delimiter is a space, this is a catch all, should the other potential delimiters not qualify, this one will almost always qualify and compares each individual word within the targeted text.

**threshold**: this is the minimum number of occurrances required to qualify as a delimiter. This is used to ensure the appropriate delimiter is used for the targeted text.


I hope this plugin serves you well, if you have any issues using it, or discover a bug, please let me know.

Email:

    johnreyn.developer@gmail.com

Social Media:

    www.linkedin.com/in/johhannas-reyn
    https://github.com/JohhannasReyn