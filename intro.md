# Chapter 1: Hello... Programming?

# Introduction

This chapter cover the basic of programming and what you need to make a sigil. Well will go through variable, control flow, loop, function, and everything else you would likely take in a beginner level programming course. We will mainly be talking about these concept in the context of `gdscript` (the sigil programming language) and so all example will be given in `gdscript`.

You should also obtain the game source code which can be download [here](https://github.com/107zxz/inscr-onln) using the `Code` button click on `Download ZIP`. You also would need the Godot engine, the specific version that the game was built on is [Godot 3.5.3](https://godotengine.org/download/3.x/windows/), download that version when messing with the game code. Also note that you should not edit the game source code to make sure that your sigil will work with any version of the game

# Formatting

Before getting into any actual programming, there a few things you need to keep in mind while programming in `gdscript` most formatting is very sensitive and may make or break your program.

First is indentation, indentation are very important the basic is choose a indent type or amount and stick with it. `gdscript` isn't strict about whenever you should use tab or space, but the amount and consistency matter, you cannot mix between tab and space and once you choose a type you need to stick with it. If you chooses 3 spaces indenting everything must be 3 spaces indenting. We will be using 1 tab for indenting for the rest of this guide.

Second is casing, casing in programming matter `int` and `Int` are very different thing and you should make sure that you casing is correct when debugging code.

# Expression vs Statement

This is a very simple distinction, expression return a value while statement does not. Expression can be use with each other while statement cannot. Unless this guide stated otherwise a syntax construct is an expression. A good rule is if it start with a keyword like `if`, `else`, `while` then it is a statement

# Variables

Variables are very simple they are like boxes that store a value so you can reuse them. Variables can have a name like label that we can put on our box. Each variable can also have a type following the box analogy, different data type are like different objects or toys we can put in our box. This is how you would declare a variable

```gdscript
var ten = 10
```

This code will make a new variable called `ten` and it will have a value of `10`. There are of course other data type that are used for different thing here some of the basic:

```
bool
int
float
Array
String
```

-   `bool` is a boolean. There are 2 types of boolean: `true` and `false`. `true` and `false` are usually used to control the flow of your program.
-   `int` is an integer. Integers are any whole number including negative number. Ex: `3`, `-4`, `0`.
-   `float` is a floating-point number. Floating point number are like integer only that they can also include a decimal portion. Ex: `1.22`, `-4.132`, `3.142`.
-   `Array` is an array or list. List can contain any other data type group together; we will talk about array later. Ex: `[1, 2, 3]`, `[true, 3.14, 10]`.
-   `String` is a string of characters. String contain any text that you would want to use, we will also cover this later. Ex: `"Hello World"`, `String`.

Here some more example of variables creation, if you see a `#` that mean the beginning of a comment, comment are note that you can make to help other read your code, they are ignore when the program is ran.

```gdscript
var pi = 3.14
var hello = "World"
var world = hello # this will set world to the same value as hello, "World"
```

After making a variable you can assign new value to it without using `var`

```gdscript
var number = 10 # make a new variable containing 10

number = 5 # change the content to 5
```

# Operator

Operators are well operation that you can do between value. `gdscript` have a few operator here are the basic arithmetic one

```gdscript
a + b
a - b
a * b
a / b
a % b
a ** b
```

These are all the basic math operation that you likely know, there are 2 different however `%` is the modulo operator usually you to find the remainder of a division and `**` is the exponent or power operator instead. You can use operator to calculate some value.

```gdscript
var sum = 1 + 4 + 19 + 11 + 2 + 4 + 3 + 1
```

Operation are evaluated following the [evaluation order](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html#operators) and if two operation is on the same priority they are evaluated left to right except a few look at the evaluation order list above to see what operation does not.

There are other operation to do comparison, we will cover them in the next section about control flow.

```gdscript
a == b
a != b
a > b
a < b
a >= b
a <= b
```

And of course some logical operator also will be cover in the next section, the code in the comment is an alternate way to write these operator this guide will focus on using the word version

```gdscript
a and b # a && b
a or b # a || b
not a # !a
```

# Array

Array are composite data type meaning they can contain multiple other data type. Array are constructed like so:

```gdscript
["One", 2, 3, "Four", true]
```

Using bracket (this guide use parenthesis, bracket and brace to mean `()`, `[]` and `{}` respectively) as delimiter and separate by `,`. Array can contain element of different type. You can access part of an array using an index. `gdscript` index start at `0` meaning element `0` is the first, `1` is the second, etc. To access an array you can use syntax like so:

```gdscript
var arr = ["One", 2, 3, "Four", true]
print(arr[0]) # "One"
print(arr[1]) # 2
# negative indexes count backward from the end
print(arr[-1]) # true
```

You can also use assignment to change part of an array

```gdscript
var arr = [1, 2, 3]
a[1] = 10
print(arr) # [1, 10, 3]
```

Appending array to another can be using the `+` operator.

```gdscript
var arr1 = [1, 2]
var arr2 = [3, 4]
print(arr1 + arr2) # [1, 2, 3, 4]
```

# Function Call

Function are a piece of code that can be reuse multiple time kind of like variable be for pieces of code instead. We will learn how to define and make our own function later but now we will use the build in one. Here how functional call look like:

```gdscript
print("Hello World")
```

There are a few thing here first is `print` which is the function name, in this case this function will print to the console. Next there is the parenthesis this signify a function call this is how `gdscript` tell variable and function apart. Lastly is what inside the parenthesis they are call arguments to the function in this case the argument is the string `"Hello World"`, function can take any amount of argument and you would separate between arguments using `,` like so `func(args1, args2, arg3)`. In summary, this line of code call the `print` function with one arguments with the value of `"Hello World"`

# Control flow

Finally something interesting, control flow are used to change the flow of your program by introducing new branch or section of code that are only run when a condition is meet. The main way to do control flow is using `if` statement. Here is how a `if` statement look:

```gdscript
if condition:
	body
```

Quite straight forward when `condition` is meet (when it equal to `true`) the `body` is run. Take note of a few thing, first the `:` at the end of the first line and that `body` is indented in. Indentation is very important and keep them in mind while debugging. Here is another example:

```gdscript
if x > 5:
	print("hello")
```

This code will see if `x` is larger than `5` then run the `print("hello")` body. `if` statement can also have a `else` block when the condition fail:

```gdscript
if x > 5:
	print("x larger than 5")
else:
	print("x is not larger than 5")
```

This code will print `x is larger than 5` if `x` is larger than `5` and `x is not larger than 5` otherwise. Another type of block you can add to a `if` statement is `elif` stand for `else if` which will execute when the `if` condition fails.

```gdscript
if x == 1:
	print(1)
elif x == 2:
	print(2)
elif x == 3:
	print(3)
else:
	print("idk")
```

This code will print `1` if x is equal to `1`, `2` is `x` is equal to `2` so on and print `idk` when all case fails. The different between `elif` and multiple `if` is when a `elif` pass it will go to the end of the statement when the block finishes.

A few operator evaluate to a boolean value like the comparison and logical operator. Comparison operator work as you would expected only equality check are done using `==`. Logical operator work like boolean normal if you ever took any boolean algebra, `and` will only evaluate to `true` if both of it operand evaluate to true, `or` will evaluate to `true` when either operand evaluate to `true`. Using these simply operator you can create some complex condition. This code below check if a number is even or odd using the modulus operator:

```gdscript
if num % 2 == 0:
	print("even")
else:
	print("odd")
```

# Loop

One important concept is looping, loop let you run a piece of code multiple time. There are 2 main types of loops `while` and `for`. `while` loop will continue to execute **while** a condition is `true`. Here a quick example:

```gdscript
while x < 5:
	print(x)
```

This will continue to print out `x` while it is still less than `5`, you can modify the variable use in the condition to fail it eventually. Here an example:

```gdscript
x = 10
while x != 0:
	print(x)
	x = x - 1
```

This code will first check if `x != 1` then if that is `true` print `x` then decrement `x` by `1` and start the cycle over again until `x != 1` fails and exit after 10 cycle. This is very common in programming so we have a special way to write it using a `for` loop.

```gdscript
for x in range(10):
	print(x)
```

This will repeat the code 10 time like it did with while loop only more concise. First `range(10)` will generate an array like so `[1, 2, 3,..., 8, 9, 10]`. `range` is a build in function that is use to generate array after the array is constructed the `for` loop will go through every element of the array assigning each to `x` run the body then go to the next element until the end of the array.

You can force a loop to break out and end immediately using `break` and use `continue` to force the loop to start a new cycle.

```gdscript
while true:
	print("get out")
	break
```

This code will print `"break out"` then exit out of the `while` loop. Note that `while true` mean the loop will run forever if you don't include a `break`

Use `for` loop if you know how many cycle you need to run and `while` when you don't.

# Defining function

Finally the final concept defining function, making your own function is quite simple here how you would do it:

```
func sum(a, b):
	sum = a + b
	return sum
```

Here we define a new function like when defining variable we use the `func` keyword to define a function next we give it a name in this case `sum`, then we need to include the parentheses and put any parameter (parameter is the name of value we give to function while argument are the actual value) we may want in this case we want 2 parameter `a` and `b`. After all of that we can define our function body in this case we calculate the sum then use a new keyword `return` to return the value. Each function can have a return and that is what we will receive if we call the function.

# Method

Methods are like functions, but they only exist on certain type. You can call a method using the following syntax:

```gdscript
x.size()
```

First you put a `.` after the value you want to call the method on in this case `x` then the method name in this case `size` and like function call a pair of parentheses with any arguments inside. Another syntax you may see is this:

```
x.body
```

While it may look like a method call it is not it is a properties access we will cover this we when we encounter it next chapter.

# Conclusion

This is will be most thing you need to make sigil, more complex topic will come up and get introduce later as you go feel free to look at the [Godot Documentation](https://docs.godotengine.org/en/3.5/) or look up online and ask other if you have any question. Next, we will be making a simple sigil that is basically a rabbit hole clone.
