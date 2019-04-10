import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        L1 = [1,2,3,4,5]
        L2 = [5,4,3,2,1]
        L3 = [53,22,47,-20,44]
        L4 = [-5,-1,-44,-35,-66]
        L5 = [1,2,3,8,5]
        L6 = []
        self.assertEqual(max_list_iter(L1),5)
        self.assertEqual(max_list_iter(L2),5)
        self.assertEqual(max_list_iter(L3),53)
        self.assertEqual(max_list_iter(L4),-1)
        self.assertEqual(max_list_iter(L5),8)
        self.assertEqual(max_list_iter(L6),None)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
       self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
       self.assertEqual(reverse_rec([1,2,3,4,5,6,7,8,9,10]),[10,9,8,7,6,5,4,3,2,1])
       self.assertEqual(reverse_rec([-1,12]),[12,-1])
       self.assertEqual(reverse_rec([1]),[1])
       self.assertEqual(reverse_rec([]),[])
       self.assertEqual(reverse_rec([-22,-6,-2,0,-4]),[-4,0,-2,-6,-22])
       with self.assertRaises(ValueError):
           reverse_rec(None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        list_val2 =[10,20,30,44,57,100]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(0, low, high, list_val), 0 )
        self.assertEqual(bin_search(10, low, high, list_val), 8 )
        self.assertEqual(bin_search(5, low, high, list_val), None )
        self.assertEqual(bin_search(11, low, high, list_val), None )
        self.assertEqual(bin_search(0, low, len([])-1, []), None )
        self.assertEqual(bin_search(0, low, len([0])-1, [0]), 0 )
        self.assertEqual(bin_search(0, low, len([4])-1, [4]), None )
        self.assertEqual(bin_search(10, low, len(list_val2)-1, list_val2), 0 )
        self.assertEqual(bin_search(5, low, len(list_val2)-1, list_val2), None )
        self.assertEqual(bin_search(-5, low, len(list_val2)-1, list_val2), None )
        self.assertEqual(bin_search(101, low, len(list_val2)-1, list_val2), None )
   
if __name__ == "__main__":
        unittest.main()

    
