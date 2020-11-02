runTests = False

### Example 1
### ---------
input("Please enter your name: ")

### Example 2
### ---------
def example2():
    name = input("Please enter your name: ")
    print("Hello, " + name + ", it is a pleasure to meet you.")
#example2() # UNCOMMENT TO PRINT


### Example 3
### ---------
def example3():
    age = input("What age are you? ")
    new_age = age + 1
    print("This time next year, you will be " + new_age + " years old.")
#example3() # UNCOMMENT TO PRINT


### Example 4
### ---------
def example4():
    age = int(input("What age are you? ")) # Note the addition of the int command on this line.
    new_age = age + 1
    print("This time next year, you will be " + str(new_age) + " years old.") # Note the addition of the str command on this line
#example4() # UNCOMMENT TO PRINT


### Task 1: fix this code so that there are no errors
### -------------------------------------------------
def task1():
    number = input("Enter a whole number: ")
    oddNumber = number * 2 - 1
    return "The " + number + "th odd number is " + oddNumber + "."
#task1() # UNCOMMENT TO PRINT


### Task 2
### ------
# Your code goes here...


### Example 5
### ---------
a = 438
b = 1560
if a * b > 1000000:
    print("The product is bigger than one million!")


### Example 6    
### ---------
def example6():
    print("five equals five:", 5 == 5)
    print("\"hello\" is the same as \"hello\":", "hello" == "hello")
    print("4 is not equal to 3:", 4 != 3)
    print("100 is greater than 99:", 100 > 99)
    print("five is greater than or equal to 5:", 5 >= 5)
#example6() # UNCOMMENT TO PRINT


### Example 7
### ---------
def example7():
    
    a = 10
    b = 12
    
    if a - b > 0:
        print("a is greater than b")
    else:
        print("a is less than or equal to b")
        
#example7() # UNCOMMENT TO PRINT


### Example 8
### ---------
a = 43

def example8a():
    
    if a < 100:
        print("a is less than 100")
    elif a < 60:
       print("a is less than 60")
    elif a < 50:
        print("a is less than 50")

#example8() # UNCOMMENT TO PRINT

# Only the first string prints because once a true condition is reached, the rest of the conditions are skipped.

# If you want all true conditions to trigger their action, you should use different if statements:

a = 43

def example8b():
    
    if a < 100:
        print("a is less than 100")
    
    if a < 60:
        print("a is less than 60")
    
    if a < 50:
        print("a is less than 50")

#example8b() # UNCOMMENT TO PRINT


### Task 3
### ------

# Edit the conditions in task 3 so that the messages print in the correct circumstances. Do not edit the messages themselves. You may change the values of a and b to check your solution.

a = 3
b = 2

def task3a(a, b):
    
    if a == b:
        return "The product of a and b is less than 100"
    elif a == b:
        return "The product of a and b is equal to 100"
    elif a == b:
        return "The product of a and b is greater than 100"
    else:
        return "Something went wrong."
        
#print(task3a(a, b)) # UNCOMMENT TO PRINT

c = 70

def task3b(c):
    
    if c == c:
        return "c is between 0 and 50 (inclusive)"
    elif c == c:
        return "c is between 51 and 100 (inclusive)"
    elif c == c:
        return "c is outside of the range 0-100"

#print(task3b(c)) # UNCOMMENT TO PRINT


### Task 4
### ------

#print(17 % 4) # UNCOMMENT TO PRINT
# This prints 1 because the remainder of 17 divided by 4 is 1.

# HINT: think about what happens when you divide an even number by 2. What about an odd number?

# Make sure your function is called parity().


### Task 5
### ------

# Your code goes here...