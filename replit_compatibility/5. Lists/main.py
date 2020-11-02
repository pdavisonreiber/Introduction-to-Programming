import unittest
from lists import *

class UnitTests(unittest.TestCase):
    def test_task1a(self):
        # Failure message:
        # Your solution to Task 1a was incorrect.
        self.assertEqual(task1a(), "red")
        
    def test_task1b(self):
        # Failure message:
        # Your solution to Task 1b was incorrect.
        self.assertEqual(task1b(), "yellow")
           
    def test_task1c(self):
        # Failure message:
        # Your solution to Task 1c was incorrect.
        self.assertEqual(task1c(), 94)
    
    def test_task2a(self):
        # Failure message:
        # Your solution to Task 2a was incorrect.
        self.assertEqual(task2a(["siren"]), ["siren", "hello", "world"])

    def test_task2b(self):
        # Failure message:
        # Your solution to Task 2b was incorrect.
        self.assertEqual(task2b(["c", "b", "a"]), 2)
        self.assertEqual(task2b(["c", "b"]), "ERROR")
    
    def test_task3(self):
        # Failure message:
        # Your solution to Task 3 was incorrect.
        self.assertEqual(task3([2, 3], [2, 3, 5]), [2, 3, 5])
        self.assertEqual(task3([2, 3, 5], [7, 11, 13]), "same length")

    def test_task4a(self):
        # Failure message:
        # Your solution to Task 4a was incorrect.
        fruits = ["banana", "kiwi", "melon", "gooseberry", "snozzberry"]
        self.assertEqual(task4a(fruits), ["banana", "melon", "gooseberry", "snozzberry"])
        self.assertEqual(task4a([2, 3, 5]), [2, 5])

    def test_task4b(self):
        # Failure message:
        # Your solution to Task 4b was incorrect.
        fruits = ["banana", "kiwi", "melon", "gooseberry", "snozzberry"]
        self.assertEqual(task4a(fruits), ["banana", "kiwi", "gooseberry", "snozzberry"])
        self.assertEqual(task4a([2, 3, 5, "melon"]), [2, 3, 5])
    
    def test_task4c(self):
        # Failure message:
        # Your solution to Task 4c was incorrect.       
        self.assertEqual(task4c(["a", "b", "c", "d"]), ["a", "b"])   
        
        
   
   
       
if __name__ == '__main__' and runTests:
    unittest.main()
    
    
    
    
    
    