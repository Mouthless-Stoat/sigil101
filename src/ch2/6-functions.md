# Functions

Function is another major concept beside variables, they allow you to reuse code like how you can reuse value like variables. In fact, function are like variables but instead of data it is for code. Let look at defining a simple function:

```gd
func test():
    print("WOAH FUNCTION")
```

The code above will define a new function call `test` and it will run the code `print("WOAH FUNCTION")` when call. It should be noted that you usually want to have function declaration **outside** of your ceremony:

```gd
extends SceneTree

func _init():
    print("other")

func stuff():
    print("This function do stuff")
```

> In this book we also use function declaration along with normal code like so:
>
> ```gd
> func a(): print("Hello")
>
> a()
> ```
>
> The function declaration will be **outside** of the `_init` function while everything else will be inside. The code above is equivalent to:
>
> ```gd
> extends SceneTree
>
> func _init():
>     a()
>
> func a(): print("Hello")
> ```
>
> Let look at another example, here a function that count to `10`:

```gd
func count():
    for i in 5:
        print(i + 1)
```

You may notice that when you run the code, it does not do anything and the output stay empty. This is because we have not **call** the function. You have call function before like `print()` and `quit()`, to call a function you need to type the function name follow by a pair of parenthesis. So to call our `count` function we can do `count()`. Now let call the function inside of `_init` to run our code:

```gd
extends SceneTree

func _init():
    count()

func count():
    for i in 5:
        print(i + 1)
```

And when you run this code you will see something like this in the output:

```
1
2
3
4
5
```

You can of course call `count()` multiple time and get a longer output:

```gd
extends SceneTree

func _init():
    count()
    count()
    count()

func count():
    for i in 5:
        print(i + 1)
```

Will give:

```hidelines=~
1
2
3
~4
~5
~1
~2
~3
~4
~5
~1
~2
~3
~4
~5
```

> The order of which function are define does not matter but usually `_init` will be put first then every other function

## Giving Function Parameters

If you look at `print()` you will notice that we can put some values between the parenthesis and it will print those values. This is call supplying a function with arguments, and to allow our function to accept arguments we must give our function parameter.

To include some parameter in our function, you can include the parameter name between the parenthesis separated by commas, while declaring the function. Like this:

```gd
func test(param_1, param_2):
    print(param_1, param_2)
```

This function above have 2 parameter and there name are `param_1` and `param_2`. We then use these parameters later in the function body to print. Parameters are like temporary variables that only the function have access to. We can then use these parameters by giving our function some arguments like so:

```gd
~func test(param_1, param_2):
~    print(param_1, param_2)
~
test(1, 10)
test("hello", " world")
```

You may notice that we always have to give the function 2 arguments this is because we define the function with 2 required parameters, we will look at optional parameters in a bit. The code above should print out:

```
110
hello world
```

> **Parameters** and **arguments** are different thing. **Arguments** is the value that our function take in and what it can use, but **parameter** is the **name** that we give to **arguments**.

## Return

`return` is a keyword you can use inside function to give the function a return value. Return value are well value that the function will evaluate to when being called, one example of a function that return a value is `range()` which we learn about in [Chapter 2.5](./5-looping.md), the function `range()` return an array when it is called. Here a simple example of a function that take in `a` and `b` and output `a + b`:

```gd
func add(a, b): return a + b
```

We can use the function like how we would with `range()`:

```gd
~func add(a, b): return a + b
~
print(add(1, 5))  # 6

var a = add(2, 3) # a is set to 3
print(a) # 3
```

> Actions that affect values outside of the function (like modifing another variable or print) are call side effect of the function. A function that only have side effect and no return are call impure, void or dirty function.

## Optional Parameters

Optional parameter are parameter to function that is well optional. These optional parameter don't need to be given when the function is called and they have a default value. Let make a simple function that print with some title text:

```gd
func better_print(content, title): print(title, ": ", content)
```

> Remember if a body is only 1 line long you don't need a new line and indent

We can use this function to print some debug messaage like this:

```gd
~func better_print(content, title): print(title, ": ", content)
~
better_print(15, "Debug")
better_print("Oh no", "Error")
better_print(10 * 8 + 1, "Calculation")
```

These will print the following to the screen for you:

```
Debug: 15
Error: Oh no
Calculation: 81
```

Now what if we just want to call `better_print(10)` and have it print `[] Debug: 10` by default. We want to make title optional and have the default value of `[] Debug`. We can achieve this like this:

```gd
func better_print(content, title = "Debug"): print(title, ": ", content)
```

Now if we call `better_print(10)` we will get `[] Debug: 10` printed out.

## Type Annotation

Let say you make the function `add()` like so:

```gd
func add(a, b): return a + b
```

We know that this function take in `a` and `b` as `int` or `float` and also return a `int` or `float`. But we can forget this fact especially with larger function, this is where type annotation came in. Type annotation allow you to add note to what the type should be. You can add type annotation to the function above like so:

```gd
func add(a: float, b: float) -> float:
    return a + b
```

We add type annotation to parameter by follow the name with a colon then the type. The return type can be added by following the parenthesis with `->` then the type follow by the colon. This function above tell us that `a` and `b` are `float` and this function `add()` will also return a `float`.

```admonish act
1. Make the code from [Chapter 2.4 Activity 1](./4-conditionals.md) into a function that the number and return `true` or `false`
2. Make the code from [Chapter 2.5 Activity 3](./5-looping.md) into a function that take in a array instead of a set array
```
