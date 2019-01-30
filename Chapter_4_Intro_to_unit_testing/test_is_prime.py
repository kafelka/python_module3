import unittest
from is_prime import is_prime
import sys

class PrimeTest(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(0))
#        self.assertTrue(sys.argv[1])
#        self.assertTrue(is_prime(3))
#        self.assertFalse(is_prime(8))
#        self.assertFalse(is_prime(4.5))
        
        

   
if __name__ == "__main__":
    unittest.main()

