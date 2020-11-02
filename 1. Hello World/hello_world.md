# Hello World

When we learn a new language, we traditionally begin by writing a one-line program that prints some version of the message "Hello world!". This is a simple programme that shows whether your computer is properly set up to run Python code.

_Now complete Tasks 1 and 2._


# Example 1
Print can be used to print more than one thing. Just separate the items with commas:
```
print("Item1", "Item2", "Item3")
```
_Now complete Task 3._


# Example 2
The `print()` function also has various parameters (settings) that you can change. Among these are end and sep: 
* `end` controls what is printed at the end of each print command, by default a new line (`\n` character.)   
* `sep` controls what is printed between each item, by default a space.

```
#code:

print("Item1", end="/")
print("Item2", end="&")
print("Item3", end="%")

#output:

Item1/Item2&Item3%
```

```
#code:

print("Item1", "Item2", "Item3", sep="~")

#output:

Item1~Item2~Item3
```

_Now do Task 4_


# Code Comments 
Note that in various places we have used the # symbol in our code. The text that follows is in in with the code, but when the code is run, it is ignored. This is useful for adding comments that explain what your code does:

What makes a good comment?
* It is short and to the point, but a complete thought. Most comments should be written in complete sentences. 
* It explains your thinking, so that when you return to the code later you will understand how you were approaching the problem. 
* It explains your thinking, so that others who work with your code will understand your overall approach to a problem. 
* It explains particularly difficult sections of code in detail. 

When should you write comments?
* When you have to think about code before writing it. 
* When you are likely to forget later exactly how you were approaching a problem. 
* When there is more than one way to solve a problem. 
* When others are unlikely to anticipate your way of thinking about a problem. 

Writing good comments is one of the clear signs of a good programmer. If you have any real interest in taking programming seriously, start using comments now. You will see them throughout the examples in these assignments.


# Example 3
```
print("Hello") # This line prints the word "Hello"
print("world") # This line prints the word "world"
# The above printed them on two seperate lines, so now I'm going to try that again using a different end string.

print("Hello", end=" ") # Here I've replaced the default newline character with a space.
print("world") # This hasn't changed.
```

Comments can also be used to turn code on and off:
```
print("Hello world") # This code runs as normal
# print("Hello Dave") # This code has been "switched off" by being made into a comment.
```

This is called "commenting out" code, and you will find it a useful tool when programming. It saves you deleting code that you might need later, but don't want to use right now.

