# Loops
Loops are used in programming whenever we want to repeat something. If you have found in your earlier code that you have had to type the same thing over and over again, or copy and paste, it is probably because you ought to be using a loop (or possibly a function).

There are two kinds of loops you can use in Python: `for` loops and `while` loops. Which one you use will depend on the particular problem you are trying to solve, but in general:
- **For** loops are used when you know in advance how many times you want to repeat.
- **While** loops are used when the number of repetitions is not known in advance.

# For Loops
The syntax for `for` loops in Python is quite simple, and follows the usual pattern of code blocks: colon at the end of the first line, indentation for code inside the block.

```
for index in range(number):
	doSomething()
```

_Try Example 1 to see how this works in practice._

The number within the range expression defines how many times the loop will repeat. To see what the index does, we can try including it within the loop.

_Try Example 2 to see what the index variable does._

As you can see, the index is a variable that increments, starting at zero (as in lists) and going up to one less than the number in the range. If we want to, we can adjust the range expression to start and end at different numbers, or even to skip some numbers. 

_Try Example 3 and 4 to see how this works._

In Example 3, the range starts at 3 and goes up to (one less than) 20. In Example 4, it goes from 4 up to 20 (not including 20) in steps of 2.

# Returning the results as a list
Often we want to return the results of a loop, not by printing one at a time, but all together in a list. For this we define an empty list before the loop, then use the `append()` function to add each result one at a time. At the end, we can print out the whole list.

_Try Example 5 to see how this works. Then try Tasks 1 to 6._


# While Loops
While loops are used when the number of repetitions is not known in advance. One really useful application is that you can allow the user to keep using your program until they want to quit. The while loop sets up an infinite loop that runs until the user does something to end the loop. This is especially useful in games.

# What is a while loop?
A while loop tests an initial condition. Look back at the chapter on conditionals and if statements to remind yourself what these are. If that condition is true, the loop starts executing. Every time the loop finishes, the condition is checked again. As long as the condition remains true, the loop keeps executing. As soon as the condition becomes false, the loop stops executing.

Here is what the syntax looks like:

```
while condition:
   Repeat this code until condition is False
Code here runs after the loop has finished
```

# Example 6
Here is a simple example, showing how a game will stay active as long as the player has enough power. 

_Try running Example 6._

# Example 7
You can also use while loops to construct lists. For example, say we want to make a list using the nth term formula for a sequence up to a certain limit.

Let's say we want to print the sequence with nth term 70 - 5n until it goes below -1000. We can do this using the code you will see in Example 7.

_Try running Example 7. Then attempt Tasks 7, 8, and 9._


# Using while loops to keep your programs running

Most of the programs we use every day run until we tell them to quit, and in the background this is often done with a while loop. In Example 8, you can see how this can be used in practice.

_Run Example 8._