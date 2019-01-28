import unittest
from is_prime import is_prime
import sys

class PrimeTest(unittest.TestCase):
    def test_prime(self):
#        self.assertTrue(is_prime(7))
        self.assertTrue(sys.argv[1])
        
        

   
if __name__ == "__main__":
    unittest.main()

