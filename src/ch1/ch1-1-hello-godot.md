# Hello Godot

The first step to making sigils is to install Godot. The specific version of Godot that the game uses is [Godot 3.5.3](godotengine.org/download/3.x/) (keep this in mind when searching for solution).

> There are way to make sigils without using Godot and the game code but this is way easier, but if you are interested however I may write one up as an Appendix.

Installing Godot is quite straightforward, just go to the page and hit download then you can extract the file. You can now open up the folder and run the `[text] Godot_v3.5.3-stable_win64.exe` file, this is how you open Godot.

## Getting the Code

The game is **open-source** (meaning the code is open for everyone to look at and download) you can find the game code [here](https://github.com/107zxz/inscr-onln). After going to that page click on `[text] Code` then `[text] Download ZIP` then you should have the game code downloaded.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/52c58fb1-a5f0-4699-885d-cd01c927d93e)

After getting the game code, extract the `.zip` file. After you extract your files, right click on the folder and choose `[text] Copy as Path`, now open Godot. In Godot, there is a `[text] Import` button to the right, click on it and paste in the path you copied earlier into the box next to the button that say `[text] Browse` (you might need to remove the `"` surrounding the path). Then simply click on `[text] Import & Edit`.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/6f83aa31-8826-4437-9dac-ff2ab5b40f41)

## Setting up PATH

For [Chapter 2](../ch02/ch02-hello-programming.md) you need to run `[text] gdscript` file outside of Godot, to do this we need to add Godot into your PATH so your computer can run these files. First find your Godot `.exe` file and rename it to `[text] godot.exe`, then right click on the file and choose `[text] Copy as Path`. Now in your search bar look up `[text] enviroment path` and hit `[text] Enter`. Now a window should pop up click on `[text] Enviromental Variables` or hit `[text] n` on your keyboard. A new window will open again, in this window look for `[text] Path` in the top box and double click on it. A new window will open once again, in this window click `[text] New` and paste in the path you copied earlier and hit `[text] Enter`. Then click on `[text] Ok` then `[text] Ok` again and then `[text] Ok` again one last time this should close all the windows.

> To check if this actually work open `[text] powershell` and type the following:
>
> ```pwsh
> > godot --help
> ```
>
> And if a lot of text that is not red pop up you should be good.

## Navigation

Godot UI might be daunting but we will talk about a few thing that you will need to follow along with this book. First on the left is your where it say `[text] Scene` is your scene tree this will be important for custom UI but not now. Next below that is the `[text] FileSystem` this is where all the game file is, you will be visiting this corner to add new file and icon to your sigil. On the right is your `[text] Inspector` and `[text] Node` tab these are again not important and are only useful later on during custom UI creation.

In the top middle of your window you should see about 4 tab `[text] 2D`, `[text] 3D`,`[text] Script`,`[text] AssetLib`. The `[text] 2D` and `[text] 3D` tab is once again not important until custom UI, what you need to remember is that `[text] Script` tab this is where you will be editing your code. When you click on it Godot will open up a code editor, we will visit this later once we start building our sigil. The `[text] AssetLib` is not important and it uses won;t be cover in this book.

A quick summary of what you need to know everything else can be safely ignore:

-   `[text] FileSystem` is where you place your file and icon for your custom sigils.
-   `[text] Script` is where you will go to edit your code

There other tab are important but not until [Chapter 9]() later on when you will learn about creating custom UI, these would be useful then:

-   `[text] Scene` is where you can see the scene hierarchy to determine how to collect node.
-   `[text] Inspector` is where you can see information about node to help you translating prototype into working code.
-   `[text] Node` is where you can see signal and connection you can from a node.
-   `[text] 2D` is where you can prototype and view your custom UI.

If you are however interested in game development in Godot, I recommended looking up some tutorial as it will help you later on but it is not require.
