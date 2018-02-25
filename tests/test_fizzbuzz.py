import unittest
from my_python_learning_scripts.fizz_buzz import fizz_buzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_FizzBuzz(self):
        expected = "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz," \
                   "Buzz,26,Fizz,28,29,FizzBuzz"
        self.assertEqual(expected, fizz_buzz(30))


if __name__ == '__main__':
    unittest.main()