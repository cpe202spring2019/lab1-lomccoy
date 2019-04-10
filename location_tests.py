import unittest
from location import *
#
class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Santa Barbera", 35, 120.7)
        loc3 = Location("CA", -57.3, 35.99)
        loc4 = Location("Austin", 0.0, -50.87)
        
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2),"Location('Santa Barbera', 35, 120.7)")
        self.assertEqual(repr(loc3),"Location('CA', -57.3, 35.99)")
        self.assertEqual(repr(loc4),"Location('Austin', 0.0, -50.87)")
    
    def test_eq(self):
            
        loc1 = Location("CA", -57.3, 35.99)
        loc2 = Location("CA", -57.3, 35.99)
        loc3 = loc1
        loc4 = Location("Austin", -57.3, 35.99)
        loc5 = Location("CA", 87.5, 35.99)
        loc6 = Location("CA", 87.5, -78.45)
        loc7 = Location("CA", -87.5, 78.45)
        self.assertTrue(loc1==loc2)
        self.assertTrue(loc1==loc3)
        self.assertTrue(loc2==loc3)
        self.assertFalse(loc1==loc4)
        self.assertFalse(loc1==loc5)
        self.assertFalse(loc1==loc6)
        self.assertFalse(loc7==loc6)
if __name__ == "__main__":
        unittest.main()
