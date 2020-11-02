# Introducing Functions

One of the core principles of any programming language is, "Don't Repeat Yourself". If you have an action that should occur many times, you can define that action once and then call that code whenever you need to carry out that action. 

This has several advantages:
- Less repetition means less code
- Less possibility for error
- Easier to make changes

# What are functions?
Functions are a set of actions that we group together, and give a name. Python has plenty of built in functions like `print()` and `max()`. We can define our own functions, which allows us to "teach" Python new behavior. Functions can have inputs and outputs, but don't necessarily need to have either.

# Syntax
The code for a function looks something like this:

```
def functionName(argument1, argument2):
	# Do whatever we want this function to do,
	#  using argument1 and argument2

functionName(value1, value2)
```

This code will not run, but it shows how functions are used in general.

# Defining a function
- Give the keyword `def`, which tells Python that you are about to *define* a function.
- Give your function a name. A variable name tells you what kind of value the variable contains; a function name should tell you what the function does.
- Give names for each argument. Arguments are inputs to the function that it needs to do its job.
- Make sure the function definition line ends with a colon.
- Inside the function, write whatever code you need to make the function do its work. Note that this code is indented to show that it is part of the function

# Using your function
- To _call_ your function, write its name followed by parentheses.
- Inside the parentheses, give the values (if any) you want the function to work with.
- These can be variables such as `current_name` and `current_age`, or they can be actual values such as 'eric' and 5.
- Note that defining a function by itself does not _run_ any code. If you want your function to run, you must call it.

# Basic Examples
Imagine that you are designing a multi-player game. After the players have entered their names, you would like to print out a welcome message for each player.

```
print("Hello, Alice, welcome to the game.")

print("Hello, Bob, welcome to the game.")

print("Hello, Charlie, welcome to the game.")
```

This has all the disadvantages we mentioned previously. If we want to slightly change the message,  for example, we would have to update three separate lines.

Functions take repeated code, put it in one place, and then you call that code when you want to use it. 

_Look at Example 1 to see what the same program looks like with a function._

In our original code, each pair of print statements was run three times, and the only difference was the name of the person being welcomed. When you see repetition like this, you can usually make your program more efficient by defining a function.

The keyword `def` tells Python that we are about to define a function. We give our function a name, `greet()` in this case. A variable's name should tell us what kind of information it holds; a function's name should tell us what the function does. We then put parentheses. Inside these parenthese we create variable names for any variable the function will need to be given in order to do its job. In this case the function will need a name to include in the welcome message. The variable `name` will hold the value that is passed into the function `greeting()`.

To use a function we give the function's name, and then put any values the function needs in order to do its work. In this case we call the function three times, each time passing it a different name.

# Example 2
In Example 2, you will see a slightly different way of doing things. Instead of printing inside the function, we have used the `return` keyword. When calling a function, we do not always want to immediately print the result, sometimes we want to use it elsewhere in the program. To do this, we return a value, which can then be saved to a variable or be used in some other way. 

When you create your own functions, you should usually return a value so that the computer can automatically check your work.

_Try Example 2._

# Example 3
In Example 3, you will see that variables can also be passed to functions when they are called.

_Try Example 3._

# Tasks
Throughout these tasks, do not rename the functions as they are given. This will allow your answers to be automatically checked.

# Task 1
Write a function that takes in a person's name, and returns a goodbye message in the form "Goodbye, Alice, thank you for playing."

# Task 2
Write a function that takes in a first name, last name, and title, and outputs the a sentence in this form: 
- "Hello, Mr Smith, or may I call you Bob?"
- "Hello, Miss Jones, or may I call you Alice?"

# Task 3: Addition Calculator
Write a function that takes in two numbers, and adds them together. Make your function print out a sentence showing the two numbers, and the result. Your sentence should be of this form:  "The sum of 3 and 5 is 8."

# Task 4: Multiplication Calculator
Do the same as task 3 but for multiplication. Your sentence should read: "The product of 8 and 9 is 72."

# Task 5: Average of Five Numbers
Write a function which takes five numbers and returns their average.