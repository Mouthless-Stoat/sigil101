# Chapter 2: Setting up

## Introduction

This chapter will help you set up your environment to start making sigil. We will be going over how to get the game code and how to navigate the Godot UI, we will also be going over alternative method to make sigils without downloading the game code.

Although not necessary, we will be talking about some tool that may help you in understanding the game code and make it a bit easier to make new sigils.

## Getting the Engine

First we will get the game engine Godot which IMF uses. The specific Godot version that IMF uses is [Godot 3.5.3](godotengine.org/download/3.x/). The installation process is quite straight forward go to the website download the file extract it and run the executable then you will have Godot Running

## Getting the Code

The game is open source on GitHub and you can get the code [here](https://github.com/107zxz/inscr-onln). After going to that page click on `Code` then `Download ZIP` and you now have the game code. To import the code into Godot first extract the `.zip` file then open up Godot. Now in Godot you may see a `Import` option click on it and navigate to where you extracted the game file, after going into that folder you will see a `project.godot` file click on that file and choose open at the bottom, this will import your game into Godot.

After this you can open the game from the front menu by double-clicking or click on the game and choose `Edit`.

## Navigating

We will talk quickly about navigating the UI but don't expect this to explain everything on screen for that you want to look somewhere else.

First on the right you will see 2 windows, the `Scene` and the `File System` don't worry about the `Scene` for now and only worry about the `File System`. This is where all the game file is and it is very useful to find where code are.

Next on top there are a few button click on `Script` for now this is where you will be editing your code. On the right there is the open script list and below that is the list of function in this script, in the center window is where you will enter your code.

Lastly in the top right conner is a few more button only focus on the triangle button that say `Play (F5)`, like the name imply this button is use to play or start the game and the shortcut is `f5` to quickly start it.

That all you need to know for now to use the engine more stuff will be introduce when they come up. We would also touch on how and where to put your custom sigil in the next chapter.

## Alternative

If you don't want to download Godot and the game code you can also make a `scripts` folder in your game directory (access using the `Open Game Directory` button in the title screen) and put your code in there. Note this guide will focus mostly on using the Godot engine because it provide a built in editor that we can use, but if you use this alternate method whenever the guide say "the sigils folder" or "the `scripts/classes/sigils` folder" it is referring to your `scripts` folder in the game directory.

## Tools

Here are some tool that you may want to have to help you decode the game. These tools mostly run in the command line (`cmd`, `powershell` or whatever your terminal is) and they help with finding text and file.

First of these tool is [`ripgrep`](https://github.com/BurntSushi/ripgrep), it lets you look for text incredibility fast this help with finding function or simply looking for a specific piece of logic you are missing. Everything on how to install and use the tool is available on the tool GitHub page take a look at it or ask other.

Secondly is [`fzf`](https://github.com/junegunn/fzf) while `ripgrep` let you look for text `fzf` look for file by name. If you have a idea of what while it is you can use `fzf` to look for the file location.

## Conclusion

Now that we finally set up our environment we can start making sigils in the next chapter. In the next chapter, we will be making a simple `Rabbit Hole` clone as our introduction to making custom sigils.
