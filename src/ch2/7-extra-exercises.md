# Extra Exercises

Now that you learn all of the concept and theory now let put them into practice and build a simple program that print out all prime number from 1 to 100. Boring? Yes, but we can't do anything interactive with just `gdscript` and using Godot to make a small game can take a long time and we need to learn alot about the engine.

So first let think about what we need, we need to check every number between 1 and 100 then print them out if they are prime. We need to find a number factor to see if it prime or not, we can use `%` which will return the remainder of a division. Let get started on making a program to count from number from 1 to 100, if you recall we can do this using loop:

```gd
for num in range(1, 101):
    print(num)
```

Let now make a function to count how many factor a number have. We can do this by again using a loop:

```gd
# Count amount of factor a number have
func count_factor(number: int) -> int:
    var amount = 0 # number to keep track of factor
    for f in range(1, number + 1): # loop thur all the number from 1 to itself
        if number % f == 0: # check if the number is divisible
            amount += 1 # increase amount if factorable
    return amount # return the amount
```

We put this inside a function so our code later can look a bit cleaner and easier to follow. Now let loop through every number from 1 to 100 and print out how many factor they have:

```gd
~# Count amount of factor a number have
~func count_factor(number: int) -> int:
~    var amount = 0 # number to keep track of factor
~    for f in range(1, number + 1): # loop thur all the number from 1 to itself
~        if number % f == 0: # check if the number is divisible
~            amount += 1 # increase amount if factorable
~    return amount # return the amount
~
for num in range(1, 101):
    print(count_factor(num))
```

Then we can check the factor amount and only print the number with 2 factors:

```gd
~# Count amount of factor a number have
~func count_factor(number: int) -> int:
~    var amount = 0 # number to keep track of factor
~    for f in range(1, number + 1): # loop thur all the number from 1 to itself
~        if number % f == 0: # check if the number is divisible
~            amount += 1 # increase amount if factorable
~    return amount # return the amount
~
for num in range(1, 101):
    if count_factor(num) == 2:
        print(num)
```

And that is it we made a program that print every prime number from 1 to 100.
