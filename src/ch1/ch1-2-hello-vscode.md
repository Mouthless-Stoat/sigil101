# Hello Vscode

Time to install [Visual Studio Code](https://code.visualstudio.com) (vscode), you can just go to that page click on download and launch the `.exe` file.

> Again you could choose not to download vscode and continue using notepad or whatever text editor you prefer. Notepad however don't really have any support to code in any languages so it very easy to make mistake while editing `json` file. If you are using other text editor like Sublime Text or Notepad++, consider looking up how to configure them to show `json` error.

## Navigation

Along the top you should see `File`, `Edit`, `Selection`, etc. Among these only `File` is really important if you click on it a menu will pop down in this menu you can find `Open File`, `Open Folder` and `Preferences`. You can use `Open File` to open well files to edit using vscode, `Open Folder` won't be use as much but will also be helpful when looking at multiple ruleset file. Lastly `Preferences` is where you can edit your setting and configure vscode to your liking. One of these setting you might want is `Auto Save` to well automatically save your file for you.

Along the left edge you should see a few icon. One of these is `Extension` this is where you can download new extension for vscode to make it more powerful. There is also the `Explorer` tab that show your current open folder and all the file in it that you can open and edit.

## Installing Extension

Go to the `Extension` tab and search for `godot-tools` and download this extension, you should also look for `Code Runner` and download that extension as well. Next you can configure `Code Runner` to run `gdscript` file, you will need this later on in [Chapter 2](../ch02/ch02-hello-programming.md).

### Configuring Code Runner

In vscode use the keybind `Ctrl-Shift-P` to open the `Command Palette` now type in the box `user setting` and you should select the option `Preferences: Open User Settings (JSON)`. This should open a new tab in vscode in that tab replace everything (it should already be empty) with the snippet below:

```json
{{#include ./listings/setting.json}}
```

This will also turn on auto save for you along with setting up `Code Runner` to run Godot file later on.
