import unittest
from loops import *

class UnitTests(unittest.TestCase):
    def test_task1(self):
        # Failure message:
        # Your solution to Task 1 was incorrect.
        self.assertEqual(task1(), [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64])
        
    def test_task2(self):
        # Failure message:
        # Your solution to Task 2 was incorrect.
        self.assertEqual(task2(), [150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200])
           
    def test_task3(self):
        # Failure message:
        # Your solution to Task 3 was incorrect.
        self.assertEqual(task3(), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_task4(self):
        # Failure message:
        # Your solution to Task 4 was incorrect.
        self.assertEqual(task4(), [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])

    def test_task5(self):
        # Failure message:
        # Your solution to Task 5 was incorrect.
        self.assertEqual(task5(), ['hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello'])
    
    def test_task6(self):
        # Failure message:
        # Your solution to Task 6 was incorrect.       
        self.assertEqual(task6(), ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa'])

    def test_task7(self):
        # Failure message:
        # Your solution to Task 7 was incorrect.       
        self.assertEqual(task7(), [8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200, 203, 206, 209, 212, 215, 218, 221, 224, 227, 230, 233, 236, 239, 242, 245, 248, 251, 254, 257, 260, 263, 266, 269, 272, 275, 278, 281, 284, 287, 290, 293, 296, 299, 302, 305, 308, 311, 314, 317, 320, 323, 326, 329, 332, 335, 338, 341, 344, 347, 350, 353, 356, 359, 362, 365, 368, 371, 374, 377, 380, 383, 386, 389, 392, 395, 398, 401, 404, 407, 410, 413, 416, 419, 422, 425, 428, 431, 434, 437, 440, 443, 446, 449, 452, 455, 458, 461, 464, 467, 470, 473, 476, 479, 482, 485, 488, 491, 494, 497, 500, 503, 506, 509, 512, 515, 518, 521, 524, 527, 530, 533, 536, 539, 542, 545, 548, 551, 554, 557, 560, 563, 566, 569, 572, 575, 578, 581, 584, 587, 590, 593, 596, 599, 602, 605, 608, 611, 614, 617, 620, 623, 626, 629, 632, 635, 638, 641, 644, 647, 650, 653, 656, 659, 662, 665, 668, 671, 674, 677, 680, 683, 686, 689, 692, 695, 698, 701, 704, 707, 710, 713, 716, 719, 722, 725, 728, 731, 734, 737, 740, 743, 746, 749, 752, 755, 758, 761, 764, 767, 770, 773, 776, 779, 782, 785, 788, 791, 794, 797, 800, 803, 806, 809, 812, 815, 818, 821, 824, 827, 830, 833, 836, 839, 842, 845, 848, 851, 854, 857, 860, 863, 866, 869, 872, 875, 878, 881, 884, 887, 890, 893, 896, 899, 902, 905, 908, 911, 914, 917, 920, 923, 926, 929, 932, 935, 938, 941, 944, 947, 950, 953, 956, 959, 962, 965, 968, 971, 974, 977, 980, 983, 986, 989, 992, 995, 998])   
        
    def test_task8(self):
        # Failure message:
        # Your solution to Task 8 was incorrect.       
        results = task8()
        self.assertTrue(results[-1] > 90 and all([result <= 90 for result in results[:-1]]))
            
    def test_task9(self):
        # Failure message:
        # Your solution to Task 8 was incorrect.       
        results = task9()
        self.assertTrue(results.count(6) == 3 and results[-1] == 6)
       
if __name__ == '__main__' and runTests:
    unittest.main()