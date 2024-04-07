# Other Tools

There are a few other tools you might want to use to help you with navigating the game code and trying to understand it:

-   `ripgrep`: a tool use to look up text and snippet of code in large project.
-   `fzf`: a tool use to look up file name and the path directly to it.

## Ripgrep

You can find and download `ripgrep` from their [GitHub repository](https://github.com/BurntSushi/ripgrep). `ripgrep` (`rg`) is a command-line tool meaning you need to run this in a command line or terminal, in our case it would mostly be `powershell` (`pwsh`). To install `rg` you can see the installation on their page, here is how to do it on Window.

First open `pwsh` this can be done by typing `powershell` into your search box on your taskbar and hit `Enter`. Next in that window you can type:

```pwsh
> winget install BurntSushi.ripgrep.MSVC
```

After a while `rg` should be install now you can use it by typing `rg` into your command line. There is a [quick start guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md) on their GitHub but the basic usage is doing:

```pwsh
> rg "text"
```

To search for a specific text in the current directory.

## Fzf

`fzf` is like `rg` but it let you look for file using the command line. Again download is on their [GitHub repository](https://github.com/junegunn/fzf). The quick Window download is:

```pwsh
> winget install fzf
```

Now you can run `fzf` in the terminal to look for file. There is also a [quick start guide](https://github.com/junegunn/fzf#usage) but the basic is you can run:

```pwsh
> fzf
```

This will open up `fzf` and now you can type in what you want and hit `Enter` to open that file.
