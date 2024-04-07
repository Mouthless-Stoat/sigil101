# Variables

> We assume from now on that you know to put code in the ceremony to get it to run.

One of the first concept we will talk about is variables, what they are and how to use them. Variable are container that we can use to store a piece of data or value to be use later. Let take a look at defining a variable

```gd
var x = 10
```

This will make a new variable call `x` and it will contain the value (or number) `10`. Variables can have different data type store in them, `x` in this case is storing a number and the number value is `10`. The type of the variable are important because it allow or more importantly disallow for certain type of operation. Let define a few more variable:

```gd
var number = 5 # new number variable
var string = "Hello" # new string variable
```

> You may have notice `[text] #` follow by some text this is call a comment, we often use these to explain code. Anything after the `[text] #` will be ignore by `gdscript`.

To define a variable you first start with the word `var`, `var` is a keyword it tell `gdscript` how to read the next few words or characters. After saying `var` we then get the variable name, in our 2 lines it is `number` and `string`. Next is the equal sign (`=`) this mark the end of our variable name and tell `gdscript` whatever value after this will be put into our variable. We first assign the value of `5` to our `number` variable and the value `"Hello"` into our `string` variable. Notice how `"Hello"` is wrap in `""` while `5` is not, this is because `"Hello"` is a string while `5` is a number. A string is simply a literal piece of text that we put in our code and a number is well a number.
