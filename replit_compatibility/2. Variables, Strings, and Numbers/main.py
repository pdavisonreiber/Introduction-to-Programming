import unittest
from variables import *

class UnitTests(unittest.TestCase):
    def test_task2(self):
        # Failure message:
        # Your solution to Task 2 was incorrect.
        self.assertEqual(task2(), "Good evening, Smith. How are you?")

    def test_task3(self):
        # Failure message:
        # Your solution to Task 3 was incorrect.
        self.assertEqual(task3(), ("this should be in lower case.", "THIS SHOULD ALL BE IN UPPER CASE", "i don't mean to seem like i am shouting: make me lower case", "Star Wars: Return Of The Jedi Should Be In Title Case"))
    
    def test_task4(self):
        # Failure message:
        # Your solution to Task 4 was incorrect.
        self.assertTrue(task4() in ["Hello Smith. How are you?", "Hello, Smith. How are you?", "Hello Smith! How are you?", "Hello, Smith! How are you?", "Hello Smith.  How are you?", "Hello, Smith.  How are you?", "Hello Smith!  How are you?", "Hello, Smith!  How are you?"])

if __name__ == '__main__' and runTests:
    unittest.main()