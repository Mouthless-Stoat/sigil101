# The Basics

Let get started on coding up something, make a new folder on your desktop or wherever it is easy for you to find. In there make a file call `main.gd` this is where you will start coding from. Then you can open up vscode and choose `Open Folder` and navigate to that folder. Now open your `main.gd` and put in this:

@f main.gd

```gd
@@snip ./listings/2-1.gd:whole
```

@c Listing 2-1: Your first program

> A box at the bottom may pop up and say `[] Couldn't connect to the GDscript language server` but don't worry about it, it is not important for what we are doing.

Now you can click the triangle run button on the top right or hit `Ctrl-Alt-N`, you may see a window quickly open but don't worry it just Godot popping up to run your code and close again. Now at bottom of your vscode window you should see something like this

```text
Godot Engine v3.5.3.stable.official.6c814135b - https://godotengine.org
OpenGL ES 3.0 Renderer: NVIDIA RTX A500 Laptop GPU/PCIe/SSE2
Async. shader compilation: OFF

Hello!
```

> I will strip the first few line for output from now on for convenience.

You can skip over the first 4 lines they are just information about Godot but at the bottom you can see `[] Hello!` this is the code that we just written and ran!

## Understanding the Example

> If you hover your mouse over these snippet and click on the eye (<i class="fa fa-eye"></i>) icon you can reveal the hidden code. This is to reduce clutter while still providing the full code for anyone that need it.

Let's break down our example and see what each part is doing, let's take a look at our first line:

```gd
@@snip ./listings/2-1.gd:first
```

This tell `gdscript` that we are extending a object or class, you won't know what this mean now but we will touch on them later in [Chapter 2.7](./ch02-07-objects.md). We are extending the `SceneTree` because it is the first thing that Godot loaded. Next we can move on to the next snippet:

```gd
@@snip ./listings/2-1.gd:func
```

This define a new function call `_init`, you will learn about function in [Chapter 2.6](./ch02-06-functions.md). The short version is Godot will execute whatever code within this function when the file is run. Next we move into the body of this function:

```gd
@@snip ./listings/2-1.gd:body
```

Take note that it is slightly indented in, this is to tell Godot that this code belong in the body of the `_init` function we just made,`[] gdscript` are very picky about these indentation, through out this book we will use 4 spaces when indenting and any snippet of code you copy from this book will follow that. Godot When you are typing code in the Godot Engine however, you can indent by hitting the `[] Tab` key this will insert a tab character instead of 4 spaces, be very careful and convert this book 4 spaces snippet to 1 tab or else your code will not run.

Anyway, in this function body, you have 2 lines `print("Hello!")` and `quit()`. The first line we call the function `print` to print the text `[] Hello!` to the screen. See that `"Hello!"` is wrap within `""`, this mean that we want `Hello!` to be a string, we will talk more about string and other type in [Chapter 2.3](./3-types.md). Lastly we do another function call `quit()` this is to tell godot to stop running the code and close the program.

## Ceremony

These lines below:

```gd
@@snip ./listings/2-1.gd:ceremony
```

Are what we call "ceremony" this mean that we always have to type these lines in our program before writing any of our own codes. Our code always have to go into the body of the `_init` function and we always end with a `quit()` to close the program. This however is only the ceremony for doing programming outside of Godot, when we get to coding sigil we will use a different ceremony for it.

```admonish act
1. Try changing the code to make it print `[] Hello World!` instead of `[] Hello!`.
2. Try removing the `quit()` line and see what happen, and why?
```
