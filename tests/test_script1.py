"""Testing the modules from script1."""
from unittest import TestCase
from my_python_learning_scripts.script1 import parse_file, get_numbers


class TestScript1(TestCase):
    """Class holds the test functions for get_numbers method."""

    def test_get_numbers(self):
        """Function should receive a list and return only the numbers."""
        self.assertEqual([1, 2, 3], get_numbers(["1", "2", "3"]))

    def test_get_numbers_intercalated(self):
        """Checks functions for numbers and non_numbers."""
        self.assertEqual([1, 2, 3], get_numbers(["1", "abc", "2", "abc2", "3"]))

    def test_get_numbers_none(self):
        """Checks function with only strings."""
        self.assertEqual([], get_numbers(["abc", "abc2"]))

    def test_get_numbers_ints(self):
        """Checks function with numbers, non_numbers and strings."""
        self.assertEqual([1, 2, 3], get_numbers(["abc", "abc2", 1, 2, 3]))

    def test_get_numbers_floats(self):
        """Checks function with floats."""
        self.assertEqual([1.0, 2.0, 3], get_numbers(["abc", "1.0", "abc2", 2.0, 3]))


class TestFiles(TestCase):
    """Tests from file."""

    def assert_from_file(self, input, expected):
        """Read from file and compares the results."""
        z = open("input.txt", "w")
        for i in input:
            z.write(str(i))
            z.write("\n")
        z.close()
        parse_file("input.txt")
        o = []
        with open("out.txt", "r") as lines:
            for line in lines:
                o.append(line.rstrip("\n"))
        self.assertEqual(expected, o)

    def test_get_numbers(self):
        """Tests the get_number function with only integers."""
        self.assert_from_file(["1", "2", "3"], ["1", "2", "3"])

    def test_get_numbers_intercalated(self):
        """Tests get_number function with integers, strings, non_numbers."""
        self.assert_from_file(["1", "abc", "2", "abc2", "3"], ["1", "2", "3"])

    def test_get_numbers_none(self):
        """Tests get_number function with string and non_number."""
        self.assert_from_file(["abc", "abc2"], [])

    def test_get_numbers_ints(self):
        """Tests get_number function with string, non_number and integers."""
        self.assert_from_file(["abc", "abc2", 1, 2, 3], ["1", "2", "3"])

    def test_get_numbers_floats(self):
        """Tests get_number function with string, non_number, and float numbers."""
        self.assert_from_file(["abc", "1.0", "abc2", 2.0, 3], ["1.0", "2.0", "3"])
