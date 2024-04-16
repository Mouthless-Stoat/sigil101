# Types

Types define how value and data interact with each other, what they can and not do. All value have a types here some basic type that you may encounter:

```gd
int        # integer
float      # floating-point number
bool       # boolean
Array      # list or Array
String     # string
Dictionary # distionary or Hashmap
```

There are more type that you may encounter later but these are the basic one. There are a few custom type that was made for IMF, that we will talk about later in [Chapter 5]().

> You may notice that some type start with a capital letter while other don't. Lowercase type (`int`, `float`, `bool`) are primitive, basically that mean they are the most basic type that `[] gdscript` support of which there are only the 3 mentioned. Any other type that start with a uppercase letter are more complex.
>
> This is also a good time to mention the concept of a literal. A literal is some value you type up literally in your code like `1` or `"Hello"` these are a integer literal and a string literal respectively.

## The Integer Type

The `int` type is for integer. Integer are any whole number, any number without a decimal part. Integer can usually meet any math need that you may want. You can create a data of the `int` type by just typing in number in your program.

```gd
print(1 + 10) # 11
print(4 * 5)  # 20
print(2 ** 3) # 8
```

## The Float Type

`float` is another number type, but unlike `int` it can contain fractional or decimal part (number like `1.5`, `3.14`, etc.). You can you use a period (`[] .`) to separate between the whole and decimal part. They function like the `int` type however allowing you to do any math operation you need.

```gd
print(1.6 + 3.3) # 4.9
```

Why do we need 2 different type of number one with decimal and one without? Because storing a float use up more space than integer, and performant and memory is crucial for game. The type of these number does matter because it affect output when doing operation between the two types.

## Operation between Float and Integer

A good rule of thumb for the output type of a operation is if the left hand and right hand is the same type the output is of the same type. If one type is a `float` the output is a `float`. Here some example:

```gd
print(1 + 1)      # int 2
print(1 / 2)      # int 0
print(10 / 3)     # int 3

print(1.0 + 1.0)  # float 2.0
print(1.0 / 2.0)  # float 0.5
print(10.0 / 3.0) # float 3.333...

print(1 + 1.0)    # float 2.0
print(1.0 / 2)    # float 0.5
print(10 / 3.0)   # float 3.333...
```

As you can see in the second and third example because both input types are `int`, the output is also an `int` and if it is not an `int` the decimal will be remove. In the case of the second example `0.5` reduce to `0` and `3.333...` reduce to `3`.

Because sometime you want to get accurate answer there are a few functions to convert types into other types the functions `float()` and `int()` are use to convert to `float` and to `int` respectively you can use them like this:

```gd
print(float(1) / 2)  # float 0.5
print(float(10) / 3) # float 3.333...
```

## The Boolean Type

Boolean is a yes or no, on or off, `true` or `false`, so the only 2 boolean values are `true` and `false`. We will use them later in the next chapter, [Chapter 2.4](./4-conditionals.md). They don't really interact with other types. There about a few operators that interact with or produce `bool`:

```gd
a and b
a or b
not a
a == b # equality
a != b # not equality
a > b  # greater than
a >= b # greater than or equal to
a < b  # less than
a <= b # less than or equal to
```

These function as comparison:

```gd
print(1 > 3)  # false
print(3 > 1)  # true
print(6 >= 6) # true
print(3 == 4) # false
print(4 != 1) # true
```

The operator `and`, `or` and `not` are logic operator and they deal with boolean. The `and` operator only return `true` if **both** input is `true` and `false` otherwise. The `or` operator return `true` if **either** input is `true` and `false` otherwise. Lastly, the `not` operator inverse the input. You can look up `Truth Table` to see a few more examples:

```gd
print(true and false) # false
print(true and true)  # true
print(true or false)  # true
print(not false)      # true
print(not true)       # false
```

> It often customary to name boolean variable in a form of a yes or no question like `is_enable` or `is_friendly`.

## The Array Type

The first "complex" type that we will talk about is the `Array` type. A `Array` is simply a collection of data store together in one large piece of data that you can access. Defining an array can be done by separating the values with a comma (`[] ,`) and enclosing every values with a pair of brackets (`[] []`):

```gd
var first_array = [1, 2, 3] # this array contains the numbers 1, 2 and 3
```

You can access element store in an array by **indexing** it. To index an array you can put the array follow by another pair of brackets with a number between called the **index**. The index of an array start with `0` and increment by `1`. You can also use a negative index to refer to the list from the end `-1` will be the last element, `-2` second last and so on:

```gd
~var first_array = [1, 2, 3]
print(first_array[0])    # 1
print(first_array[1])    # 2
print(first_array[2])    # 3

print(first_array[-1])   # 3
print(first_array[-3])   # 1

# using array literal, they can also contain value of different type
print([1.0, 5, 10][2])  # 10
```

Array also support some operation you can join or concatenate 2 arrays end to end:

```gd
print([1, 2] + [3, 4]) # [1, 2, 3, 4]
```

Array can also be involve in assignment to change the value at specific location, however you can't extend an array like this:

```gd
~var first_array = [1, 2, 3]
print(first_array) # [1, 2, 3]
first_array[1] = 10
print(first_array) # [1, 10, 3]
```

## The String Type

The `String` type represent any piece of text, you can create a string by enclosing the piece of text in quotes (`[] ""`). The text can contain any character that you want including special character like emoji:

```gd
var hello = "Hello Worlds"
var not_a_number = "1984" # this is not a number
var emoji = "🤓"
```

String function similar to array they can be index, change at index, etc:

```gd
~var string = "Test String"
print(string[5])       # S

print(string + " new") # Test String new

string[4] = "99"
print(string)          # Test99String
```

> Be careful with change string at an index, be sure you are replacing the character with another string or you will encounter unexpected result.

## The Dictionary Type

`Dictionary` is a collection of key-value pairs group together. Think of it like a group of variable together under the same top level name. You create a new dictionary using braces (`[] {}`), separating key and value with a colon (`[] :`) and key-value with commas. Your keys and values can be of any type including `Array` and `Dictionary` but they are usually not recommend.

```gd
var dict_key = "var_key"
var dict = {
    "key1": "hello",
    123: 45,
    [1, 2, 3]: "array", # array key
    dict_key: "hi" # the key here will be the string "var_key"
}
```

To access a dictionary value you can use the syntax like array indexing with the key between the bracket. If key is a string you don't need to include bracket and only need to use a period (`.`), this is called **dot notation**:

```gd
~var dict_key = "var_key"
~var dict = {
~    "key1": "hello",
~    123: 45,
~    [1, 2, 3]: "array",
~    dict_key: "hi"
~}
~
print(dict["key1"])    # hello
print(dict[123])       # 45
print(dict[[1, 2, 3]]) # array

print(dict["var_key"]) # hi
print(dict[dict_key])  # hi
print(dict.var_key)    # hi
# dict.dict_key won't work however
```

You can also assign a value to a specific key like you do with array, but different from array you can create or insert a new key like this:

```gd
var dict = {"a": 1, "b": 2}

print(dict) # {a:1, b:2}
dict.a = 10 # change the value at the key a
print(dict) # {a:10, b:2}
dict.c = 3  # add a new key c with the value 3
print(dict) # {a:10, b:2, c:3}
```

```admonish act
1. What is the return type of the following operation:
    - `1 * 7`
    - `11 / 3`
    - `1.000000 / 4`
    - `10 * 1 / 10`
    - `9.6 / 1 + 10`
2. Make a new dictionary and insert 3 new key using assignment
```
