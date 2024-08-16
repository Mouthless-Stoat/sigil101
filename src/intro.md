# Introduction

This book/guide will cover the basics of how to make custom sigil for Inscryption Multiplayer Fangame (IMF). The guide will assume you have no experience with programming or have anything set up, we will walk-through setting up everything you might need to create sigil. We do however make a few basic assumptions:

-   **You are playing on PC**. The only real way to create sigil is to use a computer. This doesn't mean using the web version on a computer, but you have to download the game file and run it locally.
-   **You are using Window**. While the bulk of this guide are not platform dependent [Chapter 1](./ch1/0-getting-started.md) and some set up was written for Window, this is simply because I am using Window.

    > We sometime run some command in the terminal (mostly `[] powershell` and mostly in [Chapter 1](./ch1/0-getting-started.md)) these command will be in a code block with and start with `[] >`, if there no `[] >` that usually mean it is the output of the previous command. You can open the terminal by typing `[] powershell` into your search bar. On other system like MacOS this would be `[] Command Prompt` make sure the find the correct name for MacOS.

-   **You have played IMF before**. If you are looking for how to create custom sigils you probably already play the game for long enough.

If you meet all these things you should be able to follow along. Now a basic rundown of the book, you probably already have a rough idea what we will be doing by looking at the side bar. There are 2 type of chapter in this book, **concept chapters** and **sigil chapters** (If you haven't notice yet this book is heavily inspire by the [Rust Bible](https://doc.rust-lang.org/book/title-page.html)). But these will give you a bit more info about each section:

-   **Chapter 1** will show you how to install things necessary for creating sigil including the [Godot Engine](https://godotengine.org) and how to navigate it. We will also download [Visual Studio Code](https://code.visualstudio.com) to write code and validate ruleset files, **Visual Studio** **_Code_** (vscode) is not the same thing as **Visual Studio** keep that in mind when searching for how to use your new fancy text editor.
-   **Chapter 2** will look at how to code in `[] gdscript`. This includes everything you would learn in a Programming Introduction course. We will go over things like variables, functions, control flows, etc.
-   **Chapter 3** will talk about how to use, edit and create rulesets and `[] json` the language rulesets are written in.
-   **Chapter 4** will be the first project chapter. We will be creating our first sigil using everything we know in the previous chapters.
-   **Chapter 5** will dig deeper into the sigil API and see what else we can do with custom sigils.
-   **Chapter 6 and 7** will all be more project chapters (except chapter 6 kinda). Chapter 6 will be recreating the `[] Detonator` sigil and chapter 7 will be creating some movement sigils.
-   **Chapter 8** will introduce custom UI for custom sigils.
-   **Chapter 9 and 10** will use the custom UI to create some more sigils similar to some Magic keywords.

By the end of this book your should be able to create almost every sigil you can think of and will also have about 6 custom sigils already made for you to use.

> Quote block like this one usually provide extra context or information. You can usually skip over them but reading them provide some more information if you want it.
