
# Conditionals

We use conditionals in programming when we have a decision to make. If one thing is true, we do A; if another thing is true, we do B. In this section you will learn how to use a kind of conditional called an if statement.

# User Input
Often as the programmer, you need to ask for input from the user of the program. You might ask them to enter their name or age for example. To do this we need to use the `input()` command. This prints a message to the user, and then waits for them to type something and press enter when they are finished typing.

_Try running Example 1._

Notice here that we included a colon and a space at the end of our message string to make it clearer to the user that they could type here.

Once the user has entered something, we need to store their answer so that we can re-use it later. For this, we use a variable.

_Try running Example 2._

The `input()` command always produces a string, even if the user enters a number. In Example 3, you will see an error because it is trying to add a string to a number.

To fix this, we need to convert the string produced by `input()` into an integer. We can do this using the `int()` command. 

When we have added one to it, we will need to convert the result back to a string, so that it can be concatenated with the other strings. We can do this using the `str()` command.

_Now try Example 4._

_Next do Task 1._

# Task 2
Create a short program that asks the user for two whole numbers, then prints out the product. Your output at the end must be a complete sentence with a capital letter and a full stop.


# If Statements
By allowing you to respond selectively to different situations and conditions, if statements open up whole new possibilities for your programs. In this section, you will learn how to test for certain conditions, and then respond in appropriate ways to those conditions.

# What is an if statement?
An if statement tests for a condition, and then responds to that condition. If the condition is true, then whatever action is listed next gets carried out. You can test for multiple conditions at the same time, and respond appropriately to each condition.

# Example 5
Look at Example 5. At the moment, it does not print anything because the product of the two numbers is less than one million. The computer has made a decision based on the size of `a * b`. Try changing the values of the variables so that it does print.

**Definition: Syntax**
> Syntax means the precise way we write code. Programming languages are very strict about correct syntax, and will give errors if things are spelt wrong or if symbols are in the wrong place. Python is particularly strict about indentation, as you will see below.

Note the syntax of if statements in Python:

```
if CONDITION:
	ACTION
```

The condition is the test that the computer does in order to make a decision. If the condition is true, the computer does the action; if not, nothing happens, and the program moves to the next line after the if statement.

Note especially the use of indentation in Python. There is a colon at the end of the line with the condition, then the next line is indented (with either two spaces, four spaces, or one tab – your choice). The indentation shows that the action line is part of the if statement. A line after which was not indented is not part of the if statement:

```
if CONDITION:
	ACTION # This line is in the if statement
ANOTHER ACTION # This line is NOT in the if statement and will always be executed, no matter whether the condition is true or false.
```

This pattern of line ending with a colon, followed by one or more indented lines is called a **code block**. You will see several more examples of code blocks in the next few lessons.

```
COMMAND DEFINING CODE BLOCK:
	LINE INSIDE CODE BLOCK
	LINE INSIDE CODE BLOCK
```

# Logical Tests
There are several symbols you can use within your if conditions to compare values:
- equality `==`
- inequality `!=`
- greater than `>` 
- greater than or equal to `>=`
- less than `<`
- less than or equal to `<=`

Equality and inequality can be used with strings as well as numbers.

_Try running Example 6._

# if-else Statements
Many times you will want to respond in two possible ways to a test. If the condition evaluates to **True**, you will want to do one thing. If the test evaluates to **False**, you will want to do something else. The **if-else** structure lets you do that easily. 

_Try Example 7 to see how this works._


# if-elif...else chains
Many times, you will want to test a series of conditions, rather than just an either-or situation. You can do this with a series of if-elif-else statements.

There is no limit to how many conditions you can test. You always need one if statement to start the chain, and you can never have more than one else statement. But you can have as many elif statements as you want.

It is important to note that in situations like this, only the first test is evaluated. In an if-elif-else chain, once a test passes the rest of the conditions are ignored.

_Try Example 8 to see this in action._

# Task 3
Edit the conditions in task 3 so that the messages print in the correct circumstances. Do not edit the messages themselves. You should change the values of a and b to check your solution.

# Task 4
Write a function called `parity()` which takes an integer as input and returns one of the strings "even" or "odd" depending on whether the integer is even or odd. You will need to know the operator `%` which is used to obtain the remainder of a division. (See the task for an example of this in use.)

# Task 5
Write a function called `usernameLengthCheck()`. It should take a string as input and determine whether it fulfils the requirements of being at least 5 characters and at most 12. You will need to use the built in `len()` function to determine the number of characters in a string. The function should return the values `True` if the username is good, and `False` if it is not. (No quotation marks required: these are values of their own not strings.)