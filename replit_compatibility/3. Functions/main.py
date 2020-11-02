import unittest
from functions import *

class UnitTests(unittest.TestCase):
    def test_task1(self):
        # Failure message:
        # Your solution to Task 1 was incorrect.
        self.assertEqual(task1("Euclid"), "Goodbye, Euclid, thank you for playing.")

    def test_task2(self):
        # Failure message:
        # Your solution to Task 2 was incorrect.
        self.assertEqual(task2("Euclid", "Roberts", "Prof"), "Hello, Prof Roberts, or may I call you Euclid?")
    
    def test_task3(self):
        # Failure message:
        # Your solution to Task 3 was incorrect.
        self.assertEqual(task3(6, 7), "The sum of 6 and 7 is 13.")

    def test_task4(self):
        # Failure message:
        # Your solution to Task 4 was incorrect.
        self.assertEqual(task4(6, 7), "The product of 8 and 9 is 72.")

    def test_task5(self):
        # Failure message:
        # Your solution to Task 5 was incorrect.
        self.assertEqual(task4(1, 2, 3, 4, 5), 3)
        self.assertEqual(task4(10, 10, 20, 35, 40), 23)

if __name__ == '__main__' and runTests:
    unittest.main()