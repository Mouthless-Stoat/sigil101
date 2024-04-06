# Hello Godot

The first step to making sigil is to install Godot. The specific version of Godot that the game uses is [Godot 3.5.3](godotengine.org/download/3.x/) (keep this in mind when searching for solution).

> There are way to make sigil without using Godot and the game code but this is way easier, but if you are interested however I may write one up as an Appendix

Installing Godot is quite straightforward, just go to the page and hit download then you can extract the file. Then open up the folder and then run the `Godot_v3.5.3-stable_win64` file, this is how you open Godot.

## Getting the Code

The game is **open-source** (meaning the code is open for everyone to look at and download) you can find the game code [here](https://github.com/107zxz/inscr-onln). After going to that page click on `Code` then `Download ZIP` then you should have the game code downloaded.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/52c58fb1-a5f0-4699-885d-cd01c927d93e)

After getting the game code extract, the `.zip` file and then open Godot. Now after you extract your files, right click on the folder and choose `Copy as Path`. In Godot, there is a `Import` button to the right, click on it and paste in the path you copy earlier into the box next to the button that say `Browse` (you might need to remove the `"` surrounding the path). Then simply click on `Import & Edit`.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/6f83aa31-8826-4437-9dac-ff2ab5b40f41)

## Navigation

Godot UI might be daunting but we will talk about a few thing that you will need to follow along with this book. First on the left is your where it say `Scene` is your scene tree this will be important for custom UI but not now. Next below that is the `FileSystem` this is where all the game file is, you will be visiting this corner to add new file and icon to your sigil. On the right is your `Inspector` and `Node` tab these are again not important and are only useful later on during custom UI creation.

In the top middle of your window you should see about 4 tab `2D`, `3D`, `Script`, `AssetLib`. The `2D` and `3D` tab is once again not important until custom UI, what you need to remember is that `Script` tab this is where you will be editing your code. When you click on it Godot will open up a code editor, we will visit this later once we start building our sigil. The `AssetLib` is not important and it uses won;t be cover in this book.

A quick summary of what you need to know everything else can be safely ignore:

-   `FileSystem` is where you place your file and icon for your custom sigils.
-   `Script` is where you will go to edit your code

There other tab are important but not until [Chapter 9]() later on when you will learn about creating custom UI, these would be useful then:

-   `Scene` is where you can see the scene hierarchy to determine how to collect node.
-   `Inspector` is where you can see information about node to help you translating prototype into working code.
-   `Node` is where you can see signal and connection you can from a node.
-   `2D` is where you can prototype and view your custom UI.

If you are however interested in game development in Godot, I recommended looking up some tutorial as it will help you later on but it is not require.
