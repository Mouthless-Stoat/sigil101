# Introduction

This book/guide will cover the basics of how to make custom sigil for Inscryption Multiplayer Fangame (IMF). The guide will assume you have no experience with programming or have anything set up, we will walk-through setting up everything you might need to create sigil. We do however make a few basic assumptions:

-   **You are playing on PC**. The only real way to create sigil is to use a computer. This doesn't mean using the web version on a computer, but you have to download the game file and run it locally.
-   **You are using a version of Window**. While most thing in this guide are not platform dependent when something does come up it usually was made with only Window in mind, this is simply because I have a Window machine and do most of my work there. All command are mainly run in `powershell` which should be already install with your Window machine, be sure to use `powershell` and not `cmd` or `Command Prompt`.
    > We sometime run some command in the terminal (mostly `powershell`) these command will be in a code block with and start with `>`, if there no `>` that usually mean it is the output of the previous command.
-   **You have played IMF before**. We will do certain thing in-game and I won't necessarily explain in much detail how to do them, here are a few examples if you can pass most or all of these you should be good to go:
    -   Make a deck in game.
    -   Open Test mode with a deck.
    -   Load a ruleset.
    -   Open the game directory.
    -   Start a fight.

If you meet all these things you should be able to follow along with this book. Now a basic rundown of the book, you probably already have a rough idea what we will be doing by looking at the side bar. There are 2 type of chapter in this book, **concept chapters** and **sigil chapters** (If you haven't notice yet this book is heavily inspire by the [Rust Bible](https://doc.rust-lang.org/book/title-page.html)). But these will give you a bit more info about each section:

-   **Chapter 1** will show you how to install most things necessary for the creation of sigil including the [Godot Engine](https://godotengine.org) and how to navigate it. We will also download [Visual Studio Code](https://code.visualstudio.com) to write our code and validate our ruleset file, **Visual Studio** **_Code_** (Vscode) is not the same thing as **Visual Studio** keep that in mind when searching for how to use your new fancy text editor.
-   **Chapter 2** will look at how to code in the sigil programming language `gdscript`. This includes everything you would learn in a Programming Introduction course. We will go over things like variables, functions, control flows, etc.
-   **Chapter 3** will talk about how to edit a ruleset and in general how to use create a ruleset, add cards and everything else you need to know to use `json` the language rulesets are written in.
-   **Chapter 4** will be the first project chapter we will encounter. We will be creating our first ever sigil in this chapter using everything we learned in the previous chapters.
-   **Chapter 5** will dig deeper into the sigil API and see what else we can also do with the sigil.
-   **Chapter 6, 7, 8** will all be more project chapters (except chapter 6 kinda). In chapter 6 we will try and recreate the `Detonator` sigil, chapter 7 will show you how to defy death and chapter 8 will teach your how to create some sigil movement.
-   **Chapter 9** will introduce you to custom UI for your sigil.
-   **Chapter 10 and 11** will use these custom UI to create some more custom sigils borrowing from magic keywords.

By the end of this book your should be able to create almost every sigil you can think of and will also have about 6 custom sigil already made for you to use.
