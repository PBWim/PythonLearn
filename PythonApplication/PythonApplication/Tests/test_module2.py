import unittest
from project import module2

class TestModule2(unittest.TestCase):
    def test_do_something(self):
        result = module2.do_something_else()
        self.assertEqual(result, "Module 2 is doing something!")

if __name__ == '__main__':
    unittest.main()
