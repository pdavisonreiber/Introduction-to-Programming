### Example 1
### ========================================
for index in range(10):
    print("Hello world")
    

### Example 2
### ========================================
def example2():
    
    for index in range(10):
        print(index, "Hello world")

#example2() # UNCOMMENT TO PRINT


### Example 3
### ========================================
def example3():
    
    for index in range(7,20):
        print(index, "Hello world")

#example3() # UNCOMMENT TO PRINT


### Example 4
### ========================================
def example4():
    
    for index in range(4, 20, 2):
        print(index, "Hello world")

#example4() # UNCOMMENT TO PRINT


### Example 5
### ========================================
def example5():
    
    results = []
    
    for index in range(4, 20, 2):
        results.append(index)
        
    return results

#print(example5()) # UNCOMMENT TO PRINT

### Task 1
### ========================================

# Edit this loop so that it returns the numbers from 13 to 64 inclusive in a list. 

def task1():

    results = []
    
    for index in range(10):
        results.append(index)
    
    return results
    
#print(task1()) # UNCOMMENT TO PRINT


### Task 2
### ========================================

# Edit this loop so that it returns the even numbers between 150 and 200 inclusive.

def task2():

    results = []
    
    for index in range(0, 10, 3):
        results.append(index)
    
    return results
    
#print(task2()) # UNCOMMENT TO PRINT


### Task 3
### ========================================

# Edit this loop so that it returns the square numbers from 1 to 100.

def task3():

    results = []
    
    for index in range(0, 10):
        results.append(index)
    
    return results
    
#print(task3()) # UNCOMMENT TO PRINT


### Task 4
### ========================================

# Edit this loop so that it returns the powers of 2 from 2 to 1024. Hint: powers can be calculated in Python using double asterisk: e.g. 2 ** 3 == 8.

def task4():

    results = []
    
    for index in range(7):
        results.append(index)
    
    return results
    
#print(task4()) # UNCOMMENT TO PRINT


### Task 5
### ========================================

# Using a loop, return a list containing the word "hello" ten times.

def task5():

    results = []
    
    # Your code goes here...
    
    return results
    
#print(task5()) # UNCOMMENT TO PRINT


### Task 6 (Extension)
### ========================================

# Using a loop, return a list containing the strings "a", "aa", "aaa", up to the string of length 20.

def task6():

    results = []
    
    # Your code goes here...
    
    return results
    
#print(task6()) # UNCOMMENT TO PRINT


### Example 6
### ========================================

def example6(): 
    # The player's power starts out at 5.
    power = 5
    
    # The player is allowed to keep playing as long as their power is over 0.
    while power > 0:
        print("You are still playing, because your power is " + str(power))
        # Your game code would go here, which includes challenges that make it
        #   possible to lose power.
        # We can represent that by just taking away from the power.
        power = power - 1
    
    print("\nOh no, your power dropped to 0! Game Over.")
        
#example6() # UNCOMMENT TO PRINT


### Example 7
### ========================================

def example7():
    
    n = 1 
    #Since this is a while loop, we need to define our own index variable. 
    
    results = []
    
    while 70 - 5 * n >= -1000:
        results.append(70 - 5 * n)
        
        n = n + 1 
        # Again, this is not a for loop, so we need to increment the index variable manually.
    
    return results

#print(example7()) # UNCOMMENT TO PRINT


### Task 7
### ========================================

# Edit this loop so that it prints the sequence 3n + 5 up to 1000.

def task7():
    
    n = 1 
    results = []
    
    while 2*n + 1 <= 100:
        results.append(2*n + 1)
        
        n += 1 
        #This is a shorter syntax for adding 1 to a variable.
        
    return results

#print(task7()) # UNCOMMENT TO PRINT


### Task 8
### ========================================

# This function prints random numbers between 1 and 6 until the first 6 appears. Change it so that it generates numbers between 1 and 100, and stops when the first number over 90 is generated.

import random

def task8():
    
    randomNumber = 0
    results = []
    
    while randomNumber != 6:
        randomNumber = random.randint(1,6)
        results.append(randomNumber)
        
    return results

#print(task8()) # UNCOMMENT TO PRINT


### Task 9 (Extension)
### ========================================

# Create a funtion which simulates rolling a dice, and stops when three 6s have been rolled. Hint: you can count the number of occurrences in a list using the count() function: e.g. [1, 1, 1, 2, 2, 3].count(1) == 3, [1, 1, 1, 2, 2, 3].count(2) == 2, [1, 1, 1, 2, 2, 3].count(3) == 1. 

import random

def task9():
    
    results = []
        
    return results

#print(task9()) # UNCOMMENT TO PRINT


### Example 8
### ========================================

def example8():
    # Start with an empty list. You can 'seed' the list with
    #  some predefined values if you like.
    names = []
    
    # Set new_name to something other than 'quit'.
    new_name = ''
    
    # Start a loop that will run until the user enters 'quit'.
    while new_name != 'quit':
        # Ask the user for a name.
        new_name = input("Please tell me someone I should know, or enter 'quit': ")
    
        # Add the new name to our list.
        if new_name != 'quit':
            names.append(new_name)
    
    # Show that the name has been added to the list.
    print(names)
    
#example8() # UNCOMMENT TO PRINT