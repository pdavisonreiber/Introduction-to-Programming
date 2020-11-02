# Variables, Strings, and Numbers

In this section, you will learn to store information in variables. You will learn about two types of data: strings, which are sets of characters, and numerical data types.


# Variables 
A variable is a named object which stores a value. You can change the value of a variable at any point. 

_Try running Example 1. Can you see how the value of the variable is changed each time?_


# Variable Naming Rules 
* Variables can only contain letters, numbers, and underscores. Variable names can start with a letter or an underscore, but can not start with a number. 
* Spaces are not allowed in variable names, so we can use underscores instead of spaces. For example, use student  name instead of "student name". 
* Another convention is to use "Camel Case" so instead of student,  name we write `studentName`. 
* You cannot use Python keywords as variable names. 
Variable names should be descriptive, so `studentName = "Thomas"` instead of `n = "Thomas"`.  
* Be careful about using the lowercase letter l and the uppercase letter O in places where they could be confused with the numbers 1 and 0. 

Examples of good variable names:
* numberOfStudents 
* answer_to_question_1
* postCode

Examples of bad variable names:
* x 
* l00p 
* integer 

_Now do Task 1._


# Example 2
There is one common error when using variables, that you will almost certainly encounter at some point. Take a look at Example 2 and see if you can figure out why it causes an error.

Let's look through this error message. First, we see it is a NameError. Then we see the file that caused the error, and a green arrow shows us what line in that file caused the error. Then we get some more specific feedback, that "name 'mesage' is not defined".

You may have already spotted the source of the error. We spelled message two different ways. Python does not care whether we use the variable name "message" or "mesage". Python only cares that the spellings of our variable names match every time we use them.

We can fix NameErrors by making sure all of our variable names are spelled consistently.

_Now do Task 2._


# Strings
Strings are the way we store text in programming. They are composed of individual characters and are indicated using double or single quotation marks.

```
string1 = "This is a double-quoted string."
string2 = 'This is a single-quoted string.'
```

# Example 3 – Changing Case
You can easily change the case of a string, to present it the way you want it to look.

_Uncomment the lines in Example 3 to see how this works._

You will see this syntax quite often, where a variable name is followed by a dot and then the name of an action, followed by a set of parentheses. The parentheses may be empty, or they may contain some values.

```
variable_name.action()
```

In this example, the word "action" is the name of a method. A method is something that can be done to a variable. The methods 'lower', 'title', and 'upper' are all functions that have been written into the Python language, which do something to strings. Later on, you will learn to write your own methods.


# Example 4 – Concatenation 
It is often very useful to be able to combine strings together into a longer string. This is called concatination, and is implemented using the + symbol. 

_Uncomment the line in Example 4 to see how this works._

If you don't know who Ada Lovelace is, you might want to go read what Wikipedia or the Computer History Museum have to say about her. She also happens to be the daughter of a famous Old Harrovian.  

_Now do Task 5._


# Example 5 – Whitespace
The term "whitespace" refers to characters that the computer is aware of, but are invisible to readers. The most common whitespace characters are spaces, tabs, and newlines.

Spaces are easy to create, because you have been using them as long as you have been using computers. Tabs and newlines are represented by special character combinations.

The two-character combination "\t" makes a tab appear in a string. Tabs can be used anywhere you like in a string.

_Try the first part of Example 5._

We often ask the user to enter some text, and they might accidentally add some whitespace before or after. Whitespace includes spaces, tabs, and newlines.

It is often a good idea to strip this whitespace from strings before you start working with them. For example, you might want to let people log in, and you probably want to treat "eric " as "eric" when you are trying to see the username eric exists on the system.  

You can strip whitespace from the left side, the right side, or both sides of a string.

_Try the second part of Example 5._


# Numbers
Dealing with simple numerical data is fairly straightforward in Python, but there are a few things you should know about.

# Example 6 – Integers
You can do all of the basic operations with integers, and everything should behave as you expect. Addition and subtraction use the standard plus and minus symbols. Multiplication uses the asterisk, and division uses a forward slash. Exponents use two asterisks.

_Try Example 6 Part 1._

You can use parentheses to modify the standard order of operations.

# Floating-Point Numbers 
Floating-point numbers refer to any number with a decimal point. Most of the time, you can think of floating point numbers as decimals, and they will behave as you expect them to. However, sometimes you will get an answer with an unexpectly long decimal part.

_Try Example 7_

This happens because of the way computers represent numbers internally; this has nothing to do with Python itself. Basically, we are used to working in powers of ten, where one tenth plus two tenths is just three tenths. But computers work in powers of two. So your computer has to represent 0.1 in a power of two, and then 0.2 as a power of two, and express their sum as a power of two. There is no exact representation for 0.3 in powers of two, and we see that in the answer to 0.1+0.2.

Python tries to hide this kind of stuff when possible. Don't worry about it much for now; just don't be surprised by it, and know that we will learn to clean up our results a little later on.

You can also get the same kind of result with other operations, as you can see in the third part of Example 7.

# Task 5 – Arithmetic 
Write a program that prints out the results of at least one calculation for each of the basic operations: addition, subtraction, multiplication, division, and exponents. 

# Task 6 – Order of Operations
- Find a calculation whose result depends on the order of operations.
- Print the result of this calculation using the standard order of operations.
- Use parentheses to force a nonstandard order of operations. Print the result of this calculation.

# Task 7 - Long Decimals 
On paper, 0.1+0.2=0.3. But you have seen that in Python, 0.1+0.2=0.30000000000000004. 
Find at least one other calculation that results in a long decimal like this. 


# Task 8 – Neat Arithmetic
- Store the results of at least 5 different calculations in separate variables. Make sure you use each operation at least once.
- Print a series of informative statements, such as "The result of the calculation 5+7 is 12." Below is an example of how to do this:

```
x = 3 + 2
print("The result of 3 plus 2 is", x)
```

# Task 9 – Neat Order of Operations 
Take your work for "Order of Operations" above. 
Instead of just printing the results, print an informative summary of the results. Show each calculation that is being done and the result of that calculation. Explain how you modified the result using parentheses. 


# The Zen of Python

The Python community is incredibly large and diverse. People are using Python in science, in medicine, in robotics, on the internet, and in any other field you can imagine. This diverse group of thinkers has developed a collective mindset about how programs should be written. If you want to understand Python and the community of Python programmers, it is a good idea to learn the ways Python programmers think.

You can easily see a set of guiding principles that is written right into the language. Try running this line of code:

```
import this
```

There is a lot here. Let's just take a few lines, and see what they mean for you as a new programmer.

> Beautiful is better than ugly.

Python programmers recognize that good code can actually be beautiful. If you come up with a particularly elegant or efficient way to solve a problem, especially a difficult problem, other Python programmers will respect your work and may even call it beautiful. There is beauty in high-level technical work.

> Explicit is better than implicit.

It is better to be clear about what you are doing, than come up with some shorter way to do something that is difficult to understand.

> Simple is better than complex.
> Complex is better than complicated.

Keep your code simple whenever possible, but recognize that we sometimes take on really difficult problems for which there are no easy solutions. In those cases, accept the complexity but avoid complication.

> Readability counts.

There are very few interesting and useful programs these days that are written and maintained entirely by one person. Write your code in a way that others can read it as easily as possible, and in a way that you will be able to read and understand it 6 months from now. This includes writing good comments in your code.

> There should be one-- and preferably only one --obvious way to do it.

There are many ways to solve most problems that come up in programming. However, most problems have a standard, well-established approach. Save complexity for when it is needed, and solve problems in the most straightforward way possible.

> Now is better than never.

No one ever writes perfect code. If you have an idea you want to implement it, write some code that works. Release it, let it be used by others, and then steadily improve it.

# Task 10 – Overall Challenges 
We have learned quite a bit so far about programming, but we haven't learned enough yet for you to go create something. In the next section, things will get much more interesting, and there will be a longer list of overall challenges.

**What I've Learned**
Write a program that uses everything you have learned in this notebook at least once. 
Write comments that label each section of your program. 
For each thing your program does, write at least one line of output that explains what your program did. 
For example, you might have one line that stores your name with some whitespace in a variable, and a second line that strips that whitespace from your name: 

```
# I learned how to strip whitespace from strings. 
name = '\t\teric'
print("I can strip tabs from my name: " + name.strip())
```