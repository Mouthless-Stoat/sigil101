# Looping

Sometime you need to repeat a section of code or run the same calculation again but with a different input, your first idea might be too copy the piece of code again to accomplish it. You may want to print the text `[] Cool` 5 times so you may do something like this:

```gd
print("Cool")
print("Cool")
print("Cool")
print("Cool")
print("Cool")
```

While this does work what if you want to print the text 10 times? 50 times? It will start to get long and unwieldy, now what if after you write the code 50 times you change your mind and want it to say `[] Hello` instead? You would have to replace every `[] Cool` with `[] Hello`. Because of this `[] gdscript` provide loop to solve this issue. The code describe above can be reduce to this 2 lines snippet:

```gd
for i in 50:
    print("Hello")
```

# While Loop

One of the most basic loop is the `while` loop, `while` loop like the name suggest will continue to loop a piece of code while a condition is meet. You can make a while loop like this:

```gd
~var condition = true
while condition:
    print("Loopping")
```

The condition like in `if` statement can be whatever you want as long as it evaluate to a `bool`. While the condition is `true` the loop will continue to loop and when it hit `false` it will stop. Here is a example of a program that count from `[] 1` to `[] 10`:

```gd
var counter = 1 # make a counter variable, to keep track

while counter <= 10: # run while the counter is less than or equal to 10
    print(counter) # print the counter
    counter += 1 # increase it by 1
```

We are checking if `counter` is also equal to `10` because we want to print `[] 10` and therefore want to loop to still run when `counter` is equal to `10`. If you want to print the text `[] Cool` 50 times using `while` loop, you would use something like this:

```gd
var counter = 0

while counter < 50:
    print("Cool")
    counter += 1
```

This follow the logic like before but now instead of printing back `counter` we print `[] Cool`. Remembering how to increment a counter and what condition to use for a `while` loop when you just want to repeat some code a set amount of time can be a bit difficult, and again `[] gdscript` provide us with a easier way to create `while` loop with a counter.

## For Loop

`for` loop is another type of loop. You can create a `for` loop easily like so:

```gd
for i in 50:
    print("Cool")
```

First you have the counter name in this case `i`, we often use `i` to label generic counter that we don't intent on using or there no name that would fit. After the counter name you will have `in` follow by an `int` of cycle or repetition you would like. The code above is the same as the `while` example we use before.

You can also replicate the counting program using `for` loop like so:

```gd
for i in 10:
    print(i + 1)
```

The reason we need to use `i + 1` instead of just `i` is because the counter start at `0` and go until it reaches one less. So `for i in 5` will have the numbers from `0` to `4`. Because we want to print out numbers from `[] 1` to `[] 10` we need to add `1` to our counter.

### For loop with Array and Dictionary

Apart from number you can also use `for` loop along side with an array or dictionary. When using with an array the `for` loop will go into every element of the array and assign it to the counter. Consider this example:

```gd
var array = [2, 4, 6, 8, 10]
for item in array:
    print(i)
```

If you run the code above it will print out all the item or element of the array. `[] gdscript` will loop through the array and assign each value to our counter `item` that we can use. The array can of course contain anything like string:

```gd
var quote = ["To be", "or not to be", "that is the question..."]
for line in quote:
    print(line)
```

When using `for` loop with a dictionary, the counter will be set to each key in the dictionary like it did with the array item:

```gd
var dict = {"a": 0, "b": 1, "c": 2}
for key in dict:
    print(keys)
```

The code will print out all the key to the dictionary line after line, if you want to loop the item instead you can use `dict[keys]` to get them.

### Using Range

`range` is a function which will create a list of number for you. `range` can take up to 3 arguments, but what each argument mean depend on the amount. If you only give `range` 1 argument that will be chosen as the end point (non-inclusive) of the array. If you give `range` 2 arguments the first will be the starting point (inclusive) and the second will be the end point (non-inclusive). And with 3 arguments `range` will act like the 2 arguments case with the third being the step. Lot of word but it very easy to understand:

```gd
print(range(5))         # [0, 1, 2, 3, 4]
print(range(3))         # [0, 1, 2]

print(range(0, 5))      # [0, 1, 2, 3, 4]
print(range(1, 3))      # [1, 2]
print(range(9, 1))      # [] because 9 > 0

print(range(0, 5, 1))   # [0, 1, 2, 3, 4]
print(range(0, 10, 2))  # [0, 2, 4, 6, 8]
print(range(1, 10, 2))  # [1, 3, 5, 7, 9]
print(range(9, 0, -1))  # [9, 8, 7, 6, 5, 4, 3, 2, 1] because -1 step backward
print(range(10, 1, -2)) # [9, 7, 5, 3, 1]
```

Because `range` generate an array you can use it in `for` loop to quickly set up a counter array for you to use.

```admonish act
1. Create a program that count every odd number from `1` to `100`.
2. Generate a range of every 4th number from 1 to 100 but in decreasing order.
3. Given this array `\[5, 6, 1, 2, 3, 2, 3, 4, 2, 4]` count how many even number is in there.
4. Given this dictionary `{"a": 10, "b": 11, "c": 1, "d": 1, "e": 10}` count how many key have the same value and what they are.
5. Given this array `\[5, 3, 2, 1, 2, 3, 2, 1, 3, 4, 3, 2, 3, 2]` count how many duplicate exist and what is the list without duplicate.
```
