# Lists
In this lesson, you will learn to store more than one valuable in a single variable. This by itself is one of the most powerful ideas in programming, and it introduces a number of other central concepts such as loops. If this section ends up making sense to you, you will be able to start writing some interesting programs, and you can be more confident that you will be able to develop overall competence as a programmer.

# Naming and Defining a List
A list is a collection of items, that is stored in a variable. The items should be related in some way, but there are no restrictions on what can be stored in a list.

Since lists are collection of objects, it is good practice to give them a plural name. If each item in your list is a car, call the list 'cars'. If each item is a dog, call your list 'dogs'. This gives you a straightforward way to refer to the entire list ('dogs'), and to a single item in the list ('dog').

In Python, square brackets designate a list. To define a list, you give the name of the list, the equals sign, and the values you want to include in your list within square brackets.

# Accessing an Item in a List
Items in a list are identified by their position in the list, starting with zero. This will almost certainly trip you up at some point. Programmers even joke about how often we all make "off-by-one" errors, so don't feel bad when you make this kind of error.

To access the first element in a list, you give the name of the list, followed by a zero in parentheses.

The number in parentheses is called the **index** of the item. Because lists start at zero, the index of an item is always one less than its position in the list. So to get the second item in the list, we need to use an index of 1.

_Try Example 1._

# Accessing the Last Item in a List
You can probably see that to get the last item in this list, we would use an index of 2. This works, but it would only work because our list has exactly three items. To get the last item in a list, no matter how long the list is, you can use an index of -1.

This syntax also works for the second to last item, the third to last, and so forth.

_Try Example 2._

# Appending Items to the End of a List
We can add an item to a list using the `append()` method. This method adds the new item to the end of the list.

_Try Example 3._

# Modifying Elements in a List
You can change the value of any element in a list if you know the position of that item.

_Try Example 4._

# Finding an Element in a List
If you want to find out the position of an element in a list, you can use the `index()` function.

This method gives an error if the requested item is not in the list.

_Try Example 5._

# Testing whether an Item is in a List
You can test whether an item is in a list using the 
`in` keyword. This is very useful in conditionals.

_Try Example 6._

# Finding the Length of a List
You can find the length of a list using the `len()` function.

_Try Example 7._

# Removing Items from a List
Hopefully you can see by now that lists are a dynamic structure. We can define an empty list and then fill it up as information comes into our program. To become really dynamic, we need some ways to remove items from a list when we no longer need them. You can remove items from a list through their position, or through their value.

# Removing items by position
If you know the position of an item in a list, you can remove that item using the `del` command. To use this approach, give the command `del` and the name of your list, with the index of the item you want to move in square brackets:

_Try Example 8._

# Removing items by value
You can also remove an item from a list if you know its value. To do this, we use the `remove()` function. Give the name of the list, followed by the word remove with the value of the item you want to remove in parentheses. Python looks through your list, finds the first item with this value, and removes it.

Be careful to note, however, that *only* the first item with this value is removed. If you have multiple items with the same value, you will have some items with this value left in your list.

_Try Example 10._

# Popping items from a list
There is a cool concept in programming called "popping" items from a collection. Every programming language has some sort of data structure similar to Python's lists. All of these structures can be used as queues, and there are various ways of processing the items in a queue.

One simple approach is to start with an empty list, and then add items to that list. When you want to work with the items in the list, you always take the last item from the list, do something with it, and then remove that item. The `pop()` function makes this easy. It removes the last item from the list, and gives it to us (it is a function which returns a value) so we can work with it. This is easier to show with an example:

_Try Example 11._

This is an example of a first-in, last-out approach. The first item in the list would be the last item processed if you kept using this approach. We will see a full implementation of this approach later on, when we learn about *while* loops.

You can actually pop any item you want from a list, by giving the index of the item you want to pop. For example, `list.pop(3)`.

_Now complete Tasks 1 to 4._
    















