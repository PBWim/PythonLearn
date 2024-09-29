import unittest
from project import module1

class TestModule1(unittest.TestCase):
    def test_do_something(self):
        result = module1.do_something()
        self.assertEqual(result, "Module 1 is doing something!")

if __name__ == '__main__':
    unittest.main()
