DuplExpellio
============

This package adds a feature to Sublime Text that allows you to quickly select or remove duplicates.

It's home is here on [GitHub](https://github.com/JohhannasReyn/DuplExpellio/).

Features
--------
  - Easily select or remove duplicate values.
  - Works for both standard text files or delimited files.
  - Automatically detects delimiters or allows custom specification via settings.
  - Customize the minimum threshold for delimiter qualification.

Installation Options
--------------------
  - **Via Package Control**:
    From within Sublime Text, navigate to `Package Control: Install Package`, search for "DuplExpellio", select it, and hit enter.
  - **Manual Installation**:
    Download this zipped folder, save it with the extension `.sublime-package` (e.g., `DuplExpellio.sublime-package`), and place it in the "Installed Packages" directory:
    - On Windows: `C:/Users/<UserName>/AppData/Roaming/Sublime Text/Installed Packages/`
    - On Mac: `~/Library/Application Support/Sublime Text/Installed Packages/`
    - On Linux: `~/.config/sublime-text/Installed Packages/`

    Restart Sublime Text if it is already open to load the package.

Usage Options
-------------
  - **Select Duplicates**:
    Navigate to `Selection -> Expand Selection to Duplicates`.
    - Default key binding: `Alt+Shift+D`.
  - **Remove Duplicates**:
    Navigate to `Edit -> Remove Duplicates`.
    - Default key binding: `Alt+Shift+X`.

    **Note**: Both commands work on the entire document if no text is selected. 
    Otherwise, they operate on the selected text only.

    **Context Menu**: To add this plugins features to the context menu, extract
    the file `Context.sublime-menu` from this package's zipped folder, or download 
    it from the repository (found here) and save it in this packages folder in the
    Sublime Text packages folder accessible from the menu via:
    `Preferences`->`Browse Packages` from there, open the directory `DuplExpellio`
    place the aforementioned file in this directory, if it doesn't exist, make it.
    Once saved to the correct location, you'll need to uncomment the appropriate 
    lines and save the file, once done, savek it and you should see the new 
    lines in the context menu

Configuration
-------------
  - **Accessing Settings**:
    Customize options via `Preferences -> Package Settings -> DuplExpellio -> Settings`.

  - **Key Bindings**:
    If the default key bindings conflict with others, they can be customized. Suggested key bindings:
    ```json
    { "keys": ["alt+shift+d"], "command": "select_duplicates" },
    { "keys": ["alt+shift+x"], "command": "remove_duplicates" }
    ```

  - **Settings Options**:
    - `delimiters`: List of delimiters used to separate entries. Default: `["\n", ",", ";", " "]`.
    - `threshold`: Minimum occurrences required to qualify as a delimiter. Default: `8`.

License
-------
- [MIT license](LICENSE)

Contact
-------
- **Email**: johnreyn.developer@gmail.com
- **LinkedIn**: [Johhannas Reyn](https://www.linkedin.com/in/johhannas-reyn)
- **GitHub**: [JohhannasReyn](https://github.com/JohhannasReyn)

Contributing
------------
Contributions are welcome! If you encounter any issues or bugs, feel free to open an issue on the GitHub repository or contact the developer directly.
