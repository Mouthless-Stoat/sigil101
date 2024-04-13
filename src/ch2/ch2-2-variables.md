# Variables

> We assume from now on that you know to put code in the ceremony to get it to run.

One of the first concept we will talk about is variables, what they are and how to use them. Variable are container that we can use to store a piece of data or value to be use later. Let take a look at defining a variable

```gd
var x = 10
```

This will make a new variable call `x` and it will contain the value (or number) `10`. Variables can have different data type store in them, `x` in this case is storing a number and the number value is `10`. The type of the variable are important because it allow or more importantly disallow for certain type of operation. Let define a few more variable:

```gd
var number = 5       # new number variable
var string = "Hello" # new string variable
```

> You may have notice `[text] #` follow by some text this is call a comment, we often use these to explain code. Anything after the `[text] #` will be ignore by`[text] gdscript`.

To define a variable you first start with the word `var`, `var` is a keyword it tell`[text] gdscript` how to read the next few words or characters. After saying `var` we then get the variable name, in our 2 lines it is `number` and `string`. Next is the equal sign (`=`) this mark the end of our variable name and tell`[text] gdscript` whatever value after this will be put into our variable.

> Variable name must follow a few rules:
>
> 1. Can't start with a number. Ex: `1a` is not possible but `a1` is.
> 2. Can't contain special character except `_`.
> 3. Can't be a list of special name like `name`, `position` and a few others. You will rarely clash with these.
>
> There are many way to name variable, this book use a naming style known as `snake_case`. It is where you use `*` to separate between words in the variable name. There are other style like `camelCase` with each new word change to have a capital letter and `PascalCase` which is like `camelCase` only the first word is also capitalized.
>
> Now is also a good time to mention that when coding your casing (capital or lowercase) matter. `new_num`, `NEW_num`, `New_num`, `new_Num`, you get the point, all of these are different variables.

We first assign the value of `5` to our `number` variable and the value `"Hello"` into our `string` variable. Notice how `"Hello"` is wrap in `""` while `5` is not, this is because `"Hello"` is a string while `5` is a number. A string is simply a literal piece of text that we put in our code and a number is well a number. Again we will talks in more details in [Chapter 2.3](./ch2-3-types.md). This is call **variable declaration statement**.

Now only defining variables won't be very useful if we don't use them. To use a variable we simply just have to type it name, following the example above if we can just input `number` to use the value store in the variables. We can use this variable instead of typing `5` every time we use it.

You may think typing out `number` is more work than just typing `5`, while this is correct if you change your mind later and want to change all `5` into `10` for example you need to go through your code and change every `5` into a `10`. But with variable we only need to change your declaration statement from `var number = 5` to `var number = 10` to change everything.

Providing a variable also give us context. If you just see a `5` in a piece of code you may not understand what it is for. But if we have a variable `wait_time` we can assume that it is the wait time we are using. Variable is like giving name to value so we can better read code.

Because of this you can declare some variable in term of other. Like this example, we give the variable `new_number` the same value as `number`:

```gd
~var number = 5
var new_number = number # have a value of 5
```

Let introduce a old friend we learn about in [Chapter 2.1](./ch2-1-the-basics.md), `print()`. We can use `print()` to output anything so we can see what going. Try the following

```gd
@@snip ./listings/2-2.gd
```

@c Listing 2-2: Very nice number

Run that code and in your terminal you should hopefully see `[text] 69`. As you can see you can print out variable by putting them in between parenthesis(`()`). This is call a **function call**, functional call allow you to execute some piece of code in this case `print()` will print to the output. We call what inside the parenthesis **arguments**, we are giving the function `print` 1 argument and it is `number`.

Also try this:

```gd
@@snip ./listings/2-3.gd
```

@c Listing 2-3: Always watching

Try to run the code and you should see `[text] 1984` printed. The function `print` can take any amount of arguments, in this case we are giving it `first` and `second` as arguments. We separate between our argument with commas (`,`). Note that `print` does not put a space between our value.

Of course we can also use string in our input like we did in [Chapter 2.1](./ch2-1-the-basics.md):

```gd
@@snip ./listings/2-4.gd
```

@c Listing 2-4: Should print `[text] Hello World`

You can see we manually inserted a space in using `" "` between our arguments. Now let learn how to compute value using our variables.

## Assignment

You can declare variable but it isn't that use full if we can't change then, it won't be call a variable if we don't vary them. To change a variable we can do this:

```gd
~var number = 5
number = 10 # number is 10 now
```

You can reassign a variable any amount of time and after you change it any time after that you use the variable the value will be replace with the most recent assignment value. Before you can assign a value to variables you need to declare the variables first. You can of course assign a value using itself

```gd
~var x = "Hello"
x = x
```

> The example above seem to violate this because it have hidden lines.

## Operators

Operators are use to compute different values.`[text] gdscript` support a few basic arithmetic operator:

```gd
a + b  # addition
a - b  # subtraction
a * b  # multiplication
a / b  # division
a % b  # modulo
a ** b # exponent
-a     # Negate
```

These are operator that you may have learn in school. The only notable thing is that we use a star (`[] *`) to represent multiplication sign like `[] ×` and `[] ⋅` that you may use in math and we use a slash (`[] /`) to do division instead of `[] ÷` or `[] :`. They work how you would expect, `print(1 + 3)` will output `[] 4`. You can also use them during variable assignment to compute a value before putting it in a variable.

```gd
var x = 10        # set x to 10
var new_x = x + x # set new_x to x + x or 10 + 10 or 20
```

The addition operator (`+`) also work with other type other than numbers. You can do addition between string as well to join them:

```gd
print("Hello" + " " + "World!") # print "Hello World!"
```

There are other interaction between types with operatitors that we will cover in [Chapter 2.3](./ch2-3-types.md). Along with some other operator that interact with other type.

## Augmented Assignment

Sometime you want to do some operation and also assign the output back to the variable. For example this is a common operation

```gd
~var x = 5
x = x + 5
print(x) # 10
```

Because this is such a common operation `[] gdscript` have special way to do this:

```gd
~var x = 5
x += 5
print(x) # 10
```

@c Listing 2-5: Augmented Assignment

You can do the operator follow by a equal sign to use this short hand.

```admonish act
It might be alot to remember so here a few example to help you practice them

1. Change Listing 2-2 to make it print `[] 1000` instead.
2. Change Listing 2-3 to contain 3 variables and print out `[] 123456`.
3. Make a variable cotaining the number `001` and try printing it and see the result.
4. Change Listing 2-5 the augmented assignment example above to add `5` to `x` the multiply it by `10`
4. Write a program that you can input into a variable as the side length and print out the volume of a cube.
```
