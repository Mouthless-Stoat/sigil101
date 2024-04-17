# Conditionals

Conditionals are use to run certain piece of code when a condition is meet. Here how would would run some code if a condition is meet:

```gd
var x = 5

if x == 5:
    print("x is 5") # this only run if x is 5
```

We start condition with `if` then the condition that we want follow by a colon and then our body. The condition should evaluate to a `bool` with `true` being execute the code in the body while `false` to skip it. This is where you would use all those boolean operator. Next the body of our conditional must be indented in like in Listing 2-1.

> Every time you type a colon, you can assume that the next line should be indented in, not only for conditional but also for functions that we will talk about [Chapter 2.6](./6-functions.md). If your body only one line you don't need to put them onto a new line at all:
>
> ```gd
> if true: print("TRUEEE")
> ```

It common to execute some code when a condition fail, we can do this using the `else` keyword. `else` is optional and can follow after a `if` block but it can not exist on it own. Here how you would use it:

```gd
if true:
    print("vrai")
else:
    print("faux")
```

There another keyword `elif` that can be include in a if block chain (often call if tree and other `elif` or else is call a branch). `elif` act like `else` but with another condition, when the first condition fail it will go to the next `elif`, and when everything fail it will go to the `else` block. This mean you can include any number of `elif` and only one else.

```gd
if true:
    print("first")
elif true:
    print("second")
elif true:
    print("third")
else:
    print("finally")
```

How is `elif` differ from just making multiple if? `elif` after finishing it block of code will skip to the end of the if tree while multiple if will execute all of them. Consider the following example:

```gd
if true: print("yes")
if true: print("yes")
if true: print("yes")
if true: print("yes")
```

That will print `[] yes` about 4 times before stopping, but consider the same example using `elif` instead:

```gd
if true: print("yes")
elif true: print("yes")
elif true: print("yes")
elif true: print("yes")
```

In this case it will only print yes once then stop without running other `elif` branch. Inside a body of a `if` block can of course include other `if` block but this is usually not recommended as there are usually better way to solve the problem. Consider the following piece of code:

```gd
var num = 6

if num > 5:
    if num < 10:
        print("The number is between 5 and 10")
```

While this piece of code work there is better way to write this logic that is usually more readable. We can utilize the logic operator and to achieves the same thing:

```gd
~var num = 6
~
if num > 5 and num < 10:
    ~print("The number is between 6 and 10")
```

# If expression

A common operation when coding is to assign a variable different value based on some condition. You can of course do something like this:

```gd
if true:
    var x = 10
else:
    var x = 3
```

This is however cumbersome if you are assigning multiple value based on different condition, consider this

```gd
~var flag1 = true
~var flag2 = false
~var flag3 = true
~
if flag1: var a = 1
else: var a = 1.5

if flag2: var b = 2
else: var b = 2.5

if flag3: var c = 3
else: var c = 3.5
```

Because of this `gdscript` have the expression ternary if which can be use to return different value based on a condition. The syntax for ternary if is as follow `true_val if condition else false_val`. So the code above can be rewritten to use ternary like so:

```gd
~var flag1 = true
~var flag2 = false
~var flag3 = true
~
var a = 1 if flag1 else 1.5
var b = 2 if flag2 else 2.5
var c = 3 if flag2 else 3.5
```

```admonish act
1. Write a program to check if a number is even or odd. You can see if a number is even or odd by checking the remainder of a division which is what the `%` operator do.
```
