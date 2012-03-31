from lifo_n import lifo_n
import unittest

class TestUnitLifoN(unittest.TestCase):
    def setUp(self):
         self.s = lifo_n()
 
    def test_lifo_n(self): 
        self.assertEqual(self.s.length(), 0)
        self.assertEqual(self.s.length(), 1)

if __name__ == "main":
    unittest.main()

