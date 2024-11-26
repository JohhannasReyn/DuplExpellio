DuplExpellio
============

This package adds a feature to Sublime Text that allows you to quickly select or remove duplicates.

It's home is here on [GitHub](https://github.com/JohhannasReyn/DuplExpellio/).

Features
--------
  - Easily select or remove duplicate values
  - Works for both standard text files or delimited files.
  - Delimiters are searched for automatically.
  - Optionally, a delimiter can be specified in this package's settings.

Installation Options
--------------------
  - From within Sublime Text's Package Control: Install Package, search for DuplExpellio, select and hit enter.
  - Or, alternatively, download this zipped folder, save it with the extension ".sublime-package"
    (i.e. "DuplExpellio.sublime-package") in your "Sublime Text/Installed Packages" directory.
    (On Windows this is usually "C://Users/<UserName>/AppData/Roaming/Sublime Text/Installed Packages/")
    If Sublime Text is already open, and you don't see it listed under:
    *Preferences -> Package Settings*, then you'll need to restart Sublime Text.

Usage Options
-------------
  - If the targeted text is not the entire document, then select 
    only the desired portion; otherwise, leave unselected.
  - Via the Context Menu: right click on the ducument or selected 
    text and select `Select or Remove Duplicates (DuplExpellio)`
  - Via the Menu Bar: *Edit -> Select or Remove Duplicates (DuplExpellio)*
  - Via Key Bindings (if enabled): Use the defined key-mapping specified in
    the sublime-keymap file. The suggested key mapping is "Ctrl+Shift+U".
  
Configuration
-------------
  - Options can be configured in DuplExpellio.sublime-settings
    To access: *Preferences -> Package Settings -> DuplExpellio*
  - For more information regarding this plugins options see the 
    `install.txt` file found in this packages `messages` folder,
    or in the settings file itself.

License & Contributing
----------------------
 - [MIT license](LICENSE)