import unittest
from conditionals import *

class UnitTests(unittest.TestCase):
    def test_task3a(self):
        # Failure message:
        # Your solution to Task 3a was incorrect.
        self.assertEqual(task3a(99), "The product of a and b is less than 100")
        self.assertEqual(task3a(-15), "The product of a and b is less than 100")
        self.assertEqual(task3a(100), "The product of a and b is equal to 100")
        self.assertEqual(task3a(101), "The product of a and b is greater than 100")
        self.assertEqual(task3a(150), "The product of a and b is greater than 100")
    
    def test_task3b(self):
        # Failure message:
        # Your solution to Task 3b was incorrect.
        self.assertEqual(task3b(30), "c is between 0 and 50 (inclusive)")
        self.assertEqual(task3b(50), "c is between 0 and 50 (inclusive)")
        self.assertEqual(task3b(51), "c is between 51 and 100 (inclusive)")
        self.assertEqual(task3b(80), "c is between 51 and 100 (inclusive)")
        self.assertEqual(task3b(100), "c is between 51 and 100 (inclusive)")
        self.assertEqual(task3b(101), "c is outside of the range 0-100")
        self.assertEqual(task3b(200), "c is outside of the range 0-100")
        self.assertEqual(task3b(-20), "c is outside of the range 0-100")

    def test_task4(self):
        # Failure message:
        # Your solution to Task 4 was incorrect.
        self.assertEqual(parity(292), "even")
        self.assertEqual(parity(577), "odd")
    
    def test_task5(self):
        # Failure message:
        # Your solution to Task 5 was incorrect.
        self.assertTrue(usernameLengthCheck("abcde"))
        self.assertTrue(usernameLengthCheck("abcdefgh"))
        self.assertTrue(usernameLengthCheck("123456789012"))
        self.assertFalse(usernameLengthCheck("abcd"))
        self.assertFalse(usernameLengthCheck("1234567890123"))
   

       
if __name__ == '__main__' and runTests:
    unittest.main()