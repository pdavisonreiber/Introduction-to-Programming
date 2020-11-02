runTests = False

### Example 1
### ========================================
students = ["Alice", "Bob", "Charlie"]

print(students[0])
print(students[1])
print(students[2])


### Example 2
### ========================================
characters = ["luke", "han", "chewie", "leia"]

character = characters[-1]
#print("The last character is ", character)
# UNCOMMENT TO PRINT

character2 = characters[-2]
#print("The second-last character is ", character2)
# UNCOMMENT TO PRINT


### Example 3
### ========================================
characters = ["luke", "han", "chewie", "leia"]
characters.append("r2d2")

#print(characters) # UNCOMMENT TO PRINT


### Example 4
### ========================================
characters = ["luke", "han", "chewie", "leia"]
characters[1] = "kylo ren"

#print(characters) # UNCOMMENT TO PRINT


### Example 5
### ========================================
characters = ["luke", "han", "chewie", "leia"]

indexOfChewie = characters.index("chewie")
#print(indexOfChewie) # UNCOMMENT TO PRINT


### Example 6
### ========================================
characters = ["luke", "han", "chewie", "leia"]

#print("luke" in characters) # UNCOMMENT TO PRINT
#print("x-wing" in characters) # UNCOMMENT TO PRINT

def example6b():
    
    item = "Alderaan"
    
    if item in characters:
        print(item + " is a character in Star Wars.")
    else:
        print(item + " isn't a character in Star Wars.")
        
#example6b() # UNCOMMENT TO PRINT


### Example 7
### ========================================
mainCharacters = ["luke", "han", "chewie", "leia", "r2d2", "c3po"]

length = len(mainCharacters)

#print("There are " + str(length) + " main characters in Star Wars." # UNCOMMENT TO PRINT


### Example 8
### ========================================
mainCharacters = ["darth vader", "luke", "han", "chewie", "leia", "r2d2", "c3po"]

del mainCharacters[0]

#print(mainCharacters) # UNCOMMENT TO PRINT


### Example 9
### ========================================
mainCharacters = ["darth vader", "luke", "han", "chewie", "leia", "r2d2", "c3po"]

mainCharacters.remove("han")

#print(mainCharacters) # UNCOMMENT TO PRINT


### Example 10
### ========================================
letters = ['a', 'b', 'c', 'a', 'b', 'c']

letters.remove('a')

#print(letters) # UNCOMMENT TO PRINT


### Example 11
### ========================================
mainCharacters = ["darth vader", "luke", "han", "chewie", "leia", "r2d2", "c3po", "obi wan"]

forceGhost = mainCharacters.pop()

#print(forceGhost, "is now a Force Ghost.") # UNCOMMENT TO PRINT
#print(mainCharacters) # UNCOMMENT TO PRINT


### Task 1
### ========================================

# Edit this code so that only the first item from the list is returned.
def task1a():
    list = ["red", "blue", "green", "yellow"]
    return list
    
#print(task1a()) # UNCOMMENT TO PRINT 

# Edit this code so that only the last item from the list is returned.
def task1b():
    list = ["red", "blue", "green", "yellow"]
    return list
    
#print(task1b()) # UNCOMMENT TO PRINT 

    
# In this part, you do not know how long the list is. Edit the code so that the second last element is returned.
def task1c():
    list = [i for i in range(7, 100, 3)]
    return list
    
#print(task1c()) # UNCOMMENT TO PRINT 


### Task 2
### ========================================

# Write a function which takes a list as input and returns the list with the additional elements "hello" and "world".
def task2a(list):
    
    return 0
    
#print(task2a()) # UNCOMMENT TO PRINT 

# Write a function which takes a list as input and returns the index of the element "a" if it is contained in the list. If it is not contained in the list, you should return the string "ERROR".

def task2b(list):
    if "a" in list:
        return 0
    else:
        return 0
    
#print(task2b()) # UNCOMMENT TO PRINT 


### Task 3
### ========================================

# Write a function which takes two different lists and returns the longer of the two. If both are the same length, return the string "same length".

def task3(list1, list2):
    return 0


### Task 4
### ========================================
fruits = ["banana", "kiwi", "melon", "gooseberry", "snozzberry"]

def task4a(fruits):
    # Add some code here to delete "kiwi" from the list.    
    # You must use the del command
    return fruits
    
#print(task4a(fruits)) # UNCOMMENT TO PRINT

def task4b(fruits):
    # Add some code her to delete "melon". 
    # You must use the remove() command.
    return fruits
    
#print(task4b(fruits)) # UNCOMMENT TO PRINT

    
# Write a function which takes a list as input, removes the first two items using the pop() command, and returns a list containing just these two items. So an input of [2, 3, 5, 7, 11] would give an output of [2, 3].

def task4c(list):
    return [0, 0]
    